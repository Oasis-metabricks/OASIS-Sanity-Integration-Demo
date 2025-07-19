#!/usr/bin/env python3
"""
STAR Integration Script
Installs generated templates and integrates with STAR system
"""

import os
import json
import subprocess
import requests
from typing import Dict, List, Optional
from star_template_generator import STARTemplateGenerator

class STARIntegration:
    """Integrates generated templates with STAR system"""
    
    def __init__(self, project_id: str, api_token: str, dataset: str = "production"):
        self.project_id = project_id
        self.api_token = api_token
        self.dataset = dataset
        self.base_url = f"https://{project_id}.api.sanity.io/v2021-06-07"
        self.template_generator = STARTemplateGenerator(project_id, api_token, dataset)
        
    def generate_and_install_templates(self) -> List[str]:
        """Generate templates and prepare them for STAR installation"""
        print("🔨 Generating and preparing STAR templates...")
        
        # Generate template files
        templates = self.template_generator.get_sanity_templates()
        installed_templates = []
        
        for template in templates:
            try:
                # Generate template files
                template_file = self.template_generator.generate_template_files(template)
                
                # Prepare for STAR installation
                template_id = template.get('_id')
                template_name = template.get('name', 'unnamed')
                
                # Create installation metadata
                installation_data = {
                    "template_id": template_id,
                    "template_name": template_name,
                    "template_file": template_file,
                    "template_type": template.get('templateType'),
                    "platform": template.get('platform'),
                    "installed_path": f"templates/{template_name}_{template_id}",
                    "ready_for_star": True
                }
                
                installed_templates.append(installation_data)
                print(f"✅ Prepared template: {template_name}")
                
            except Exception as e:
                print(f"❌ Failed to prepare template {template.get('name', 'Unknown')}: {e}")
        
        return installed_templates
    
    def create_star_project(self, template_data: Dict, content_data: Dict) -> Dict:
        """Create a STAR project using the template and content"""
        print(f"🚀 Creating STAR project with template: {template_data.get('template_name')}")
        
        # This would integrate with the actual STAR.LightAsync() method
        # For now, we'll create a project structure that STAR can use
        
        project_name = f"{template_data.get('template_name')}_{content_data.get('_id', 'content')}"
        project_dir = f"star_projects/{project_name}"
        
        if not os.path.exists("star_projects"):
            os.makedirs("star_projects")
        
        if os.path.exists(project_dir):
            import shutil
            shutil.rmtree(project_dir)
        
        os.makedirs(project_dir)
        
        # Create STAR project structure
        self._create_star_project_structure(project_dir, template_data, content_data)
        
        # Create STAR configuration
        star_config = self._create_star_config(template_data, content_data)
        
        with open(os.path.join(project_dir, "star-config.json"), "w") as f:
            json.dump(star_config, f, indent=2)
        
        print(f"✅ STAR project created: {project_dir}")
        
        return {
            "project_name": project_name,
            "project_dir": project_dir,
            "template_used": template_data.get('template_name'),
            "content_used": content_data.get('title', 'Unknown'),
            "star_config": star_config
        }
    
    def _create_star_project_structure(self, project_dir: str, template_data: Dict, content_data: Dict):
        """Create the STAR project file structure"""
        
        # Create main project files
        project_file = f'''<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  
  <ItemGroup>
    <PackageReference Include="NextGenSoftware.OASIS.API.Core" Version="3.3.1" />
    <PackageReference Include="NextGenSoftware.OASIS.API.ONODE.Core" Version="3.3.1" />
    <PackageReference Include="NextGenSoftware.OASIS.STAR" Version="3.3.1" />
  </ItemGroup>
</Project>
'''
        
        with open(os.path.join(project_dir, f"{template_data.get('template_name')}.csproj"), "w") as f:
            f.write(project_file)
        
        # Create Program.cs
        program_file = '''using NextGenSoftware.OASIS.STAR;
using NextGenSoftware.OASIS.API.Core.Enums;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorPages();
builder.Services.AddServerSideBlazor();

// Initialize OASIS
await STAR.IgniteStarAsync();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.MapBlazorHub();
app.MapFallbackToPage("/_Host");

app.Run();
'''
        
        with open(os.path.join(project_dir, "Program.cs"), "w") as f:
            f.write(program_file)
        
        # Create Pages directory
        pages_dir = os.path.join(project_dir, "Pages")
        os.makedirs(pages_dir)
        
        # Create _Host.cshtml
        host_file = '''@page "/"
@using Microsoft.AspNetCore.Components.Web
@namespace {PROJECT_NAME}.Pages
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{PROJECT_NAME}</title>
    <base href="~/" />
    <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" />
    <link href="css/site.css" rel="stylesheet" />
    <link href="{PROJECT_NAME}.styles.css" rel="stylesheet" />
    <component type="typeof(HeadOutlet)" render-mode="ServerPrerendered" />
</head>
<body>
    <component type="typeof(App)" render-mode="ServerPrerendered" />

    <div id="blazor-error-ui">
        <environment include="Staging,Production">
            An error has occurred. This application may no longer respond until reloaded.
        </environment>
        <environment include="Development">
            An unhandled exception has occurred. See browser dev tools for details.
        </environment>
        <a href="" class="reload">Reload</a>
        <a class="dismiss">🗙</a>
    </div>

    <script src="_framework/blazor.server.js"></script>
</body>
</html>
'''.replace('{PROJECT_NAME}', template_data.get('template_name', 'STARApp'))
        
        with open(os.path.join(pages_dir, "_Host.cshtml"), "w") as f:
            f.write(host_file)
        
        # Create _Layout.cshtml
        layout_file = '''@using Microsoft.AspNetCore.Components.Web
@namespace {PROJECT_NAME}.Pages
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>@ViewData["Title"] - {PROJECT_NAME}</title>
    <base href="~/" />
    <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" />
    <link href="css/site.css" rel="stylesheet" />
    <link href="{PROJECT_NAME}.styles.css" rel="stylesheet" />
    <component type="typeof(HeadOutlet)" render-mode="ServerPrerendered" />
    <component type="typeof(HeadOutlet)" render-mode="ServerPrerendered" />
</head>
<body>
    @RenderBody()

    <div id="blazor-error-ui">
        <environment include="Staging,Production">
            An error has occurred. This application may no longer respond until reloaded.
        </environment>
        <environment include="Development">
            An unhandled exception has occurred. See browser dev tools for details.
        </environment>
        <a href="" class="reload">Reload</a>
        <a class="dismiss">🗙</a>
    </div>

    <script src="_framework/blazor.server.js"></script>

    @await RenderSectionAsync("Scripts", required: false)
</body>
</html>
'''.replace('{PROJECT_NAME}', template_data.get('template_name', 'STARApp'))
        
        with open(os.path.join(pages_dir, "_Layout.cshtml"), "w") as f:
            f.write(layout_file)
        
        # Create wwwroot directory
        wwwroot_dir = os.path.join(project_dir, "wwwroot")
        os.makedirs(wwwroot_dir)
        os.makedirs(os.path.join(wwwroot_dir, "css"))
        
        # Create basic CSS
        css_file = '''html { font-size: 14px; }

@media (min-width: 768px) {
  html { font-size: 16px; }
}

.btn:focus, .btn:active:focus, .btn-link.nav-link:focus, .form-control:focus, .form-check-input:focus {
  box-shadow: 0 0 0 0.1rem white, 0 0 0 0.25rem #258cfb;
}

html { position: relative; min-height: 100%; }

body { margin-bottom: 60px; }
.footer { position: absolute; bottom: 0; width: 100%; white-space: nowrap; line-height: 60px; }
'''
        
        with open(os.path.join(wwwroot_dir, "css", "site.css"), "w") as f:
            f.write(css_file)
        
        # Create App.razor
        app_razor = '''<Router AppAssembly="@typeof(App).Assembly">
    <Found Context="routeData">
        <RouteView RouteData="@routeData" DefaultLayout="@typeof(MainLayout)" />
        <FocusOnNavigate RouteData="@routeData" Selector="h1" />
    </Found>
    <NotFound>
        <PageTitle>Not found</PageTitle>
        <LayoutView Layout="@typeof(MainLayout)">
            <p role="alert">Sorry, there's nothing at this address.</p>
        </LayoutView>
    </NotFound>
</Router>
'''
        
        with open(os.path.join(project_dir, "App.razor"), "w") as f:
            f.write(app_razor)
        
        # Create _Imports.razor
        imports_razor = '''@using System.Net.Http
@using Microsoft.AspNetCore.Authorization
@using Microsoft.AspNetCore.Components.Authorization
@using Microsoft.AspNetCore.Components.Forms
@using Microsoft.AspNetCore.Components.Routing
@using Microsoft.AspNetCore.Components.Web
@using Microsoft.AspNetCore.Components.Web.Virtualization
@using Microsoft.JSInterop
@using {PROJECT_NAME}
@using {PROJECT_NAME}.Shared
'''.replace('{PROJECT_NAME}', template_data.get('template_name', 'STARApp'))
        
        with open(os.path.join(project_dir, "_Imports.razor"), "w") as f:
            f.write(imports_razor)
        
        # Create Shared directory and MainLayout.razor
        shared_dir = os.path.join(project_dir, "Shared")
        os.makedirs(shared_dir)
        
        main_layout = '''@inherits LayoutComponentBase

<PageTitle>{PROJECT_NAME}</PageTitle>

<div class="page">
    <div class="sidebar">
        <NavMenu />
    </div>

    <main>
        <div class="top-row px-4">
            <a href="https://docs.microsoft.com/aspnet/" target="_blank">About</a>
        </div>

        <article class="content px-4">
            @Body
        </article>
    </main>
</div>
'''.replace('{PROJECT_NAME}', template_data.get('template_name', 'STARApp'))
        
        with open(os.path.join(shared_dir, "MainLayout.razor"), "w") as f:
            f.write(main_layout)
        
        # Create NavMenu.razor
        nav_menu = '''﻿<div class="top-row ps-3 navbar navbar-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="">{PROJECT_NAME}</a>
        <button title="Navigation menu" class="navbar-toggler" @onclick="ToggleNavMenu">
            <span class="navbar-toggler-icon"></span>
        </button>
    </div>
</div>

<div class="@NavMenuCssClass nav-scrollable" @onclick="ToggleNavMenu">
    <nav class="flex-column">
        <div class="nav-item px-3">
            <NavLink class="nav-link" href="" Match="NavLinkMatch.All">
                <span class="oi oi-home" aria-hidden="true"></span> Home
            </NavLink>
        </div>
    </nav>
</div>

@code {{
    private bool collapseNavMenu = true;

    private string? NavMenuCssClass => collapseNavMenu ? "collapse" : null;

    private void ToggleNavMenu()
    {{
        collapseNavMenu = !collapseNavMenu;
    }}
}}
'''.replace('{PROJECT_NAME}', template_data.get('template_name', 'STARApp'))
        
        with open(os.path.join(shared_dir, "NavMenu.razor"), "w") as f:
            f.write(nav_menu)
        
        # Create NavMenu.razor.css
        nav_menu_css = '''.navbar-toggler {
    background-color: rgba(255, 255, 255, 0.1);
}

.top-row {
    height: 3.5rem;
    background-color: rgba(0,0,0,0.4);
}

.navbar-brand {
    font-size: 1.1rem;
}

.oi {
    width: 2rem;
    font-size: 1.1rem;
    vertical-align: text-top;
    top: -2px;
}

.nav-item {
    font-size: 0.9rem;
    padding-bottom: 0.5rem;
}

    .nav-item:first-of-type {
        padding-top: 1rem;
    }

    .nav-item:last-of-type {
        padding-bottom: 1rem;
    }

    .nav-item a {
        color: #d7d7d7;
        border-radius: 4px;
        height: 3rem;
        display: flex;
        align-items: center;
        line-height: 3rem;
    }

.nav-item a.active {
    background-color: rgba(255,255,255,0.25);
    color: white;
}

.nav-item a:hover {
    background-color: rgba(255,255,255,0.1);
    color: white;
}

@media (min-width: 641px) {
    .navbar-toggler {
        display: none;
    }

    .collapse {
        /* Never collapse the sidebar for wide screens */
        display: block;
    }
    
    .nav-scrollable {
        /* Allow sidebar to scroll for tall menus */
        height: calc(100vh - 3.5rem);
        overflow-y: auto;
    }
}
'''
        
        with open(os.path.join(shared_dir, "NavMenu.razor.css"), "w") as f:
            f.write(nav_menu_css)
        
        # Create MainLayout.razor.css
        main_layout_css = '''@page "/"

.page {
    position: relative;
    display: flex;
    flex-direction: column;
}

.main {
    flex: 1;
}

.sidebar {
    background-image: linear-gradient(180deg, rgb(5, 39, 103) 0%, #3a0647 70%);
}

.top-row {
    background-color: #f7f7f7;
    border-bottom: 1px solid #d6d5d5;
    justify-content: flex-end;
    height: 3.5rem;
    display: flex;
    align-items: center;
}

    .top-row a, .top-row .btn-link {
        white-space: nowrap;
        margin-left: 1.5rem;
        text-decoration: none;
    }

    .top-row a:hover, .top-row .btn-link:hover {
        text-decoration: underline;
    }

    .top-row a:first-child {
        overflow: hidden;
        text-overflow: ellipsis;
    }

@media (max-width: 640.98px) {
    .top-row:not(.auth) {
        display: none;
    }

    .top-row.auth {
        justify-content: space-between;
    }

    .top-row a, .top-row .btn-link {
        margin-left: 0;
    }
}

@media (min-width: 641px) {
    .page {
        flex-direction: row;
    }

    .sidebar {
        width: 250px;
        height: 100vh;
        position: sticky;
        top: 0;
    }

    .main > div {
        padding-left: 2rem !important;
        padding-right: 1.5rem !important;
    }
}
'''
        
        with open(os.path.join(shared_dir, "MainLayout.razor.css"), "w") as f:
            f.write(main_layout_css)
    
    def _create_star_config(self, template_data: Dict, content_data: Dict) -> Dict:
        """Create STAR configuration for the project"""
        
        return {
            "projectName": template_data.get('template_name'),
            "projectDescription": f"Generated from {template_data.get('template_name')} template",
            "oappType": "Blazor",
            "genesisType": "ZomesAndHolonsOnly",
            "templateId": template_data.get('template_id'),
            "contentId": content_data.get('_id'),
            "contentType": content_data.get('_type'),
            "walletIntegration": template_data.get('walletIntegration', {}),
            "interactiveFeatures": template_data.get('interactiveFeatures', []),
            "platform": template_data.get('platform', 'web'),
            "generatedAt": datetime.utcnow().isoformat(),
            "starVersion": "3.3.1",
            "oasisVersion": "3.3.1"
        }
    
    def get_content_for_templates(self) -> List[Dict]:
        """Get content from Sanity that can be used with templates"""
        print("📖 Fetching content from Sanity...")
        
        query = '''
        *[_type in ["retreat", "housing", "carbonCredit", "contentCreatorSimple"]] {
          _id,
          _type,
          title,
          description,
          avatar,
          status
        }
        '''
        
        response = self._execute_query(query)
        if "error" in response:
            print(f"❌ Error fetching content: {response['error']}")
            return []
        
        return response.get('result', [])
    
    def match_templates_to_content(self, templates: List[Dict], content: List[Dict]) -> List[Dict]:
        """Match templates to appropriate content"""
        matches = []
        
        for template in templates:
            template_type = template.get('template_type')
            
            for item in content:
                content_type = item.get('_type')
                
                # Match template types to content types
                if (template_type == 'retreat_booking' and content_type == 'retreat') or \
                   (template_type == 'housing_purchase' and content_type == 'housing') or \
                   (template_type == 'carbon_trading' and content_type == 'carbonCredit') or \
                   (template_type == 'content_monetization' and content_type == 'contentCreatorSimple'):
                    
                    matches.append({
                        "template": template,
                        "content": item,
                        "match_score": 1.0
                    })
        
        return matches
    
    def _execute_query(self, query: str) -> Dict:
        """Execute a Sanity query"""
        url = f"{self.base_url}/data/query/{self.dataset}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        params = {"query": query}
        
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Query failed: {response.status_code}")
                return {"error": response.text}
        except Exception as e:
            print(f"❌ Error executing query: {e}")
            return {"error": str(e)}

def demo_star_integration():
    """Demonstrate complete STAR integration"""
    
    print("🌟 STAR Integration Demo")
    print("=" * 50)
    
    # Initialize integration
    project_id = "dvvkusmi"
    api_token = "skc5ZCFCJ5o6xkoen6m3IidL61XifaoOHPYzcYBLFn2GIO3xxUAuSdfVTmyP8lYFTNo0e0MUvfyPNwNuj60pWcnm7XBQVIWH6bD47MAQ5KQBV0JnYReovwvIoXnuPvTYoEvRJFXlkWzs78zkD99cNL0DDWXTEBnStg2b6hmLmZDvQGoZTaNy"
    
    integration = STARIntegration(project_id, api_token)
    
    # Step 1: Generate and install templates
    print("\n1️⃣ Generating and installing templates...")
    installed_templates = integration.generate_and_install_templates()
    
    if not installed_templates:
        print("❌ No templates were prepared")
        return
    
    print(f"✅ Prepared {len(installed_templates)} templates")
    
    # Step 2: Get content
    print("\n2️⃣ Fetching content...")
    content = integration.get_content_for_templates()
    
    if not content:
        print("❌ No content found")
        return
    
    print(f"✅ Found {len(content)} content items")
    
    # Step 3: Match templates to content
    print("\n3️⃣ Matching templates to content...")
    matches = integration.match_templates_to_content(installed_templates, content)
    
    if not matches:
        print("❌ No matches found")
        return
    
    print(f"✅ Found {len(matches)} template-content matches")
    
    # Step 4: Create STAR projects
    print("\n4️⃣ Creating STAR projects...")
    created_projects = []
    
    for match in matches[:3]:  # Limit to first 3 for demo
        try:
            project = integration.create_star_project(match['template'], match['content'])
            created_projects.append(project)
            print(f"✅ Created project: {project['project_name']}")
        except Exception as e:
            print(f"❌ Failed to create project: {e}")
    
    print(f"\n🎉 Created {len(created_projects)} STAR projects!")
    print("=" * 50)
    
    for project in created_projects:
        print(f"📁 Project: {project['project_name']}")
        print(f"   Template: {project['template_used']}")
        print(f"   Content: {project['content_used']}")
        print(f"   Directory: {project['project_dir']}")
        print()
    
    print("🚀 Next steps:")
    print("1. Build and run STAR projects")
    print("2. Deploy to production")
    print("3. Integrate with OASIS wallet system")
    
    return integration

if __name__ == "__main__":
    from datetime import datetime
    demo_star_integration() 