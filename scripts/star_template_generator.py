#!/usr/bin/env python3
"""
STAR Template Generator
Converts Sanity template records into actual OAPP template files for STAR
"""

import os
import json
import uuid
import shutil
import zipfile
from datetime import datetime
from typing import Dict, List, Optional
import requests

class STARTemplateGenerator:
    """Generates actual OAPP template files from Sanity template records"""
    
    def __init__(self, project_id: str, api_token: str, dataset: str = "production"):
        self.project_id = project_id
        self.api_token = api_token
        self.dataset = dataset
        self.base_url = f"https://{project_id}.api.sanity.io/v2021-06-07"
        self.template_output_dir = "generated_templates"
        
        # Create output directory
        if not os.path.exists(self.template_output_dir):
            os.makedirs(self.template_output_dir)
    
    def get_sanity_templates(self) -> List[Dict]:
        """Get all STAR templates from Sanity"""
        print("📋 Fetching STAR templates from Sanity...")
        
        query = '''
        *[_type == "starTemplate"] {
          _id,
          name,
          description,
          templateType,
          platform,
          templateCode,
          walletIntegration,
          interactiveFeatures,
          deploymentStatus,
          createdBy,
          version,
          tags
        }
        '''
        
        response = self._execute_query(query)
        if "error" in response:
            print(f"❌ Error fetching templates: {response['error']}")
            return []
        
        return response.get('result', [])
    
    def generate_template_files(self, template_data: Dict) -> str:
        """Generate actual template files from Sanity template data"""
        template_name = template_data.get('name', 'unnamed_template')
        template_id = template_data.get('_id', str(uuid.uuid4()))
        
        print(f"🔨 Generating template files for: {template_name}")
        
        # Create template directory
        template_dir = os.path.join(self.template_output_dir, f"{template_name}_{template_id}")
        if os.path.exists(template_dir):
            shutil.rmtree(template_dir)
        os.makedirs(template_dir)
        
        # Generate template structure based on type
        template_type = template_data.get('templateType', 'retreat_booking')
        platform = template_data.get('platform', 'web')
        
        if template_type == 'retreat_booking':
            self._generate_retreat_booking_template(template_data, template_dir)
        elif template_type == 'housing_purchase':
            self._generate_housing_purchase_template(template_data, template_dir)
        elif template_type == 'carbon_trading':
            self._generate_carbon_trading_template(template_data, template_dir)
        elif template_type == 'content_monetization':
            self._generate_content_monetization_template(template_data, template_dir)
        else:
            self._generate_generic_template(template_data, template_dir)
        
        # Create OAPP template metadata
        self._create_oapp_template_metadata(template_data, template_dir)
        
        # Create .oapptemplate file
        template_file = self._create_oapptemplate_file(template_dir, template_name)
        
        print(f"✅ Template files generated: {template_file}")
        return template_file
    
    def _generate_retreat_booking_template(self, template_data: Dict, template_dir: str):
        """Generate retreat booking template files"""
        
        # Create Blazor template structure
        blazor_dir = os.path.join(template_dir, "Blazor")
        os.makedirs(blazor_dir)
        
        # Main page
        main_page = '''@page "/retreat/{RetreatId}"
@using NextGenSoftware.OASIS.API.Core.Holons
@using NextGenSoftware.OASIS.API.Core.Interfaces
@inject IOASISAPI OASISAPI
@inject NavigationManager Navigation

<h3>Retreat Booking</h3>

<div class="retreat-details">
    <h4>@RetreatTitle</h4>
    <p>@RetreatDescription</p>
    <div class="retreat-info">
        <p><strong>Location:</strong> @RetreatLocation</p>
        <p><strong>Dates:</strong> @RetreatStartDate - @RetreatEndDate</p>
        <p><strong>Price:</strong> $@RetreatPrice</p>
        <p><strong>Available Spots:</strong> @AvailableSpots</p>
    </div>
</div>

<div class="booking-form">
    <h4>Book Your Spot</h4>
    <div class="form-group">
        <label>Number of Participants:</label>
        <input type="number" @bind="Participants" min="1" max="@AvailableSpots" />
    </div>
    <div class="form-group">
        <label>Payment Method:</label>
        <select @bind="PaymentMethod">
            <option value="crypto">Crypto</option>
            <option value="credit_card">Credit Card</option>
            <option value="karma">Karma Points</option>
        </select>
    </div>
    <button class="btn btn-primary" @onclick="BookRetreat">Book Now</button>
</div>

@code {
    [Parameter]
    public string RetreatId { get; set; }
    
    private string RetreatTitle { get; set; }
    private string RetreatDescription { get; set; }
    private string RetreatLocation { get; set; }
    private string RetreatStartDate { get; set; }
    private string RetreatEndDate { get; set; }
    private decimal RetreatPrice { get; set; }
    private int AvailableSpots { get; set; }
    private int Participants { get; set; } = 1;
    private string PaymentMethod { get; set; } = "crypto";
    
    protected override async Task OnInitializedAsync()
    {
        await LoadRetreatData();
    }
    
    private async Task LoadRetreatData()
    {
        // Load retreat data from OASIS
        // This would integrate with the actual OASIS API
    }
    
    private async Task BookRetreat()
    {
        // Process booking with wallet integration
        // This would integrate with OASIS wallet system
    }
}
'''
        
        with open(os.path.join(blazor_dir, "RetreatBooking.razor"), "w") as f:
            f.write(main_page)
        
        # Create project file
        project_file = '''<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  
  <ItemGroup>
    <PackageReference Include="NextGenSoftware.OASIS.API.Core" Version="3.3.1" />
    <PackageReference Include="NextGenSoftware.OASIS.API.ONODE.Core" Version="3.3.1" />
  </ItemGroup>
</Project>
'''
        
        with open(os.path.join(blazor_dir, "RetreatBooking.csproj"), "w") as f:
            f.write(project_file)
    
    def _generate_housing_purchase_template(self, template_data: Dict, template_dir: str):
        """Generate housing purchase template files"""
        
        blazor_dir = os.path.join(template_dir, "Blazor")
        os.makedirs(blazor_dir)
        
        main_page = '''@page "/housing/{ProjectId}"
@using NextGenSoftware.OASIS.API.Core.Holons
@using NextGenSoftware.OASIS.API.Core.Interfaces
@inject IOASISAPI OASISAPI
@inject NavigationManager Navigation

<h3>Housing Project Investment</h3>

<div class="housing-details">
    <h4>@ProjectName</h4>
    <p>@ProjectDescription</p>
    <div class="project-info">
        <p><strong>Location:</strong> @ProjectLocation</p>
        <p><strong>Total Units:</strong> @TotalUnits</p>
        <p><strong>Available Shares:</strong> @AvailableShares</p>
        <p><strong>Share Price:</strong> $@SharePrice</p>
        <p><strong>Expected ROI:</strong> @ExpectedROI%</p>
    </div>
</div>

<div class="investment-form">
    <h4>Invest in Housing</h4>
    <div class="form-group">
        <label>Number of Shares:</label>
        <input type="number" @bind="SharesToPurchase" min="1" max="@AvailableShares" />
    </div>
    <div class="form-group">
        <label>Payment Method:</label>
        <select @bind="PaymentMethod">
            <option value="crypto">Crypto</option>
            <option value="credit_card">Credit Card</option>
            <option value="bank_transfer">Bank Transfer</option>
        </select>
    </div>
    <button class="btn btn-primary" @onclick="PurchaseShares">Invest Now</button>
</div>

@code {
    [Parameter]
    public string ProjectId { get; set; }
    
    private string ProjectName { get; set; }
    private string ProjectDescription { get; set; }
    private string ProjectLocation { get; set; }
    private int TotalUnits { get; set; }
    private int AvailableShares { get; set; }
    private decimal SharePrice { get; set; }
    private decimal ExpectedROI { get; set; }
    private int SharesToPurchase { get; set; } = 1;
    private string PaymentMethod { get; set; } = "crypto";
    
    protected override async Task OnInitializedAsync()
    {
        await LoadHousingData();
    }
    
    private async Task LoadHousingData()
    {
        // Load housing project data from OASIS
    }
    
    private async Task PurchaseShares()
    {
        // Process investment with wallet integration
    }
}
'''
        
        with open(os.path.join(blazor_dir, "HousingInvestment.razor"), "w") as f:
            f.write(main_page)
    
    def _generate_carbon_trading_template(self, template_data: Dict, template_dir: str):
        """Generate carbon trading template files"""
        
        blazor_dir = os.path.join(template_dir, "Blazor")
        os.makedirs(blazor_dir)
        
        main_page = '''@page "/carbon/{ProjectId}"
@using NextGenSoftware.OASIS.API.Core.Holons
@using NextGenSoftware.OASIS.API.Core.Interfaces
@inject IOASISAPI OASISAPI
@inject NavigationManager Navigation

<h3>Carbon Credit Trading</h3>

<div class="carbon-details">
    <h4>@ProjectName</h4>
    <p>@ProjectDescription</p>
    <div class="project-info">
        <p><strong>Certification:</strong> @Certification</p>
        <p><strong>Carbon Offset:</strong> @CarbonOffset tons CO2</p>
        <p><strong>Available Credits:</strong> @AvailableCredits</p>
        <p><strong>Credit Price:</strong> $@CreditPrice</p>
        <p><strong>Environmental Impact:</strong> @EnvironmentalImpact</p>
    </div>
</div>

<div class="trading-form">
    <h4>Trade Carbon Credits</h4>
    <div class="form-group">
        <label>Action:</label>
        <select @bind="TradingAction">
            <option value="buy">Buy Credits</option>
            <option value="sell">Sell Credits</option>
        </select>
    </div>
    <div class="form-group">
        <label>Number of Credits:</label>
        <input type="number" @bind="CreditsAmount" min="1" />
    </div>
    <div class="form-group">
        <label>Payment Method:</label>
        <select @bind="PaymentMethod">
            <option value="crypto">Crypto</option>
            <option value="credit_card">Credit Card</option>
        </select>
    </div>
    <button class="btn btn-primary" @onclick="TradeCredits">Execute Trade</button>
</div>

@code {
    [Parameter]
    public string ProjectId { get; set; }
    
    private string ProjectName { get; set; }
    private string ProjectDescription { get; set; }
    private string Certification { get; set; }
    private decimal CarbonOffset { get; set; }
    private int AvailableCredits { get; set; }
    private decimal CreditPrice { get; set; }
    private string EnvironmentalImpact { get; set; }
    private string TradingAction { get; set; } = "buy";
    private int CreditsAmount { get; set; } = 1;
    private string PaymentMethod { get; set; } = "crypto";
    
    protected override async Task OnInitializedAsync()
    {
        await LoadCarbonData();
    }
    
    private async Task LoadCarbonData()
    {
        // Load carbon project data from OASIS
    }
    
    private async Task TradeCredits()
    {
        // Process carbon credit trading
    }
}
'''
        
        with open(os.path.join(blazor_dir, "CarbonTrading.razor"), "w") as f:
            f.write(main_page)
    
    def _generate_content_monetization_template(self, template_data: Dict, template_dir: str):
        """Generate content monetization template files"""
        
        blazor_dir = os.path.join(template_dir, "Blazor")
        os.makedirs(blazor_dir)
        
        main_page = '''@page "/content/{ContentId}"
@using NextGenSoftware.OASIS.API.Core.Holons
@using NextGenSoftware.OASIS.API.Core.Interfaces
@inject IOASISAPI OASISAPI
@inject NavigationManager Navigation

<h3>Content Creator Platform</h3>

<div class="content-details">
    <h4>@ContentTitle</h4>
    <p>@ContentDescription</p>
    <div class="creator-info">
        <p><strong>Creator:</strong> @CreatorName</p>
        <p><strong>Category:</strong> @Category</p>
        <p><strong>Engagement:</strong> @Engagement followers</p>
        <p><strong>Monetization:</strong> @MonetizationStatus</p>
    </div>
</div>

<div class="monetization-options">
    <h4>Support Creator</h4>
    <div class="form-group">
        <label>Support Type:</label>
        <select @bind="SupportType">
            <option value="tip">Tip Creator</option>
            <option value="subscription">Monthly Subscription</option>
            <option value="nft">Purchase NFT</option>
        </select>
    </div>
    <div class="form-group">
        <label>Amount:</label>
        <input type="number" @bind="SupportAmount" min="1" step="0.01" />
    </div>
    <div class="form-group">
        <label>Payment Method:</label>
        <select @bind="PaymentMethod">
            <option value="crypto">Crypto</option>
            <option value="credit_card">Credit Card</option>
            <option value="karma">Karma Points</option>
        </select>
    </div>
    <button class="btn btn-primary" @onclick="SupportCreator">Support Creator</button>
</div>

@code {
    [Parameter]
    public string ContentId { get; set; }
    
    private string ContentTitle { get; set; }
    private string ContentDescription { get; set; }
    private string CreatorName { get; set; }
    private string Category { get; set; }
    private int Engagement { get; set; }
    private string MonetizationStatus { get; set; }
    private string SupportType { get; set; } = "tip";
    private decimal SupportAmount { get; set; } = 5.00m;
    private string PaymentMethod { get; set; } = "crypto";
    
    protected override async Task OnInitializedAsync()
    {
        await LoadContentData();
    }
    
    private async Task LoadContentData()
    {
        // Load content data from OASIS
    }
    
    private async Task SupportCreator()
    {
        // Process creator support with wallet integration
    }
}
'''
        
        with open(os.path.join(blazor_dir, "ContentMonetization.razor"), "w") as f:
            f.write(main_page)
    
    def _generate_generic_template(self, template_data: Dict, template_dir: str):
        """Generate generic template files"""
        
        blazor_dir = os.path.join(template_dir, "Blazor")
        os.makedirs(blazor_dir)
        
        # Use the template code from Sanity if available
        template_code = template_data.get('templateCode', '')
        
        if template_code:
            # Parse and use the custom template code
            main_page = f'''@page "/dapp"
@using NextGenSoftware.OASIS.API.Core.Holons
@using NextGenSoftware.OASIS.API.Core.Interfaces
@inject IOASISAPI OASISAPI
@inject NavigationManager Navigation

<h3>Custom dApp</h3>

<div class="dapp-content">
    <!-- Custom template code will be injected here -->
    {template_code}
</div>

@code {{
    protected override async Task OnInitializedAsync()
    {{
        // Initialize custom dApp
    }}
}}
'''
        else:
            main_page = '''@page "/dapp"
@using NextGenSoftware.OASIS.API.Core.Holons
@using NextGenSoftware.OASIS.API.Core.Interfaces
@inject IOASISAPI OASISAPI
@inject NavigationManager Navigation

<h3>Generic dApp Template</h3>

<div class="dapp-content">
    <p>This is a generic dApp template. Customize as needed.</p>
</div>

@code {
    protected override async Task OnInitializedAsync()
    {
        // Initialize dApp
    }
}
'''
        
        with open(os.path.join(blazor_dir, "GenericDApp.razor"), "w") as f:
            f.write(main_page)
    
    def _create_oapp_template_metadata(self, template_data: Dict, template_dir: str):
        """Create OAPP template metadata file"""
        
        metadata = {
            "id": template_data.get('_id', str(uuid.uuid4())),
            "name": template_data.get('name', 'Unnamed Template'),
            "description": template_data.get('description', ''),
            "version": template_data.get('version', '1.0.0'),
            "templateType": template_data.get('templateType', 'generic'),
            "platform": template_data.get('platform', 'web'),
            "createdBy": template_data.get('createdBy', {}),
            "walletIntegration": template_data.get('walletIntegration', {}),
            "interactiveFeatures": template_data.get('interactiveFeatures', []),
            "tags": template_data.get('tags', []),
            "createdAt": datetime.utcnow().isoformat(),
            "oappType": "Blazor",
            "launchTarget": "index.html"
        }
        
        with open(os.path.join(template_dir, "template-metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2)
    
    def _create_oapptemplate_file(self, template_dir: str, template_name: str) -> str:
        """Create .oapptemplate file from template directory"""
        
        template_file = os.path.join(self.template_output_dir, f"{template_name}.oapptemplate")
        
        with zipfile.ZipFile(template_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(template_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, template_dir)
                    zipf.write(file_path, arc_name)
        
        return template_file
    
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

def demo_star_template_generation():
    """Demonstrate STAR template generation from Sanity"""
    
    print("🌟 STAR Template Generation Demo")
    print("=" * 50)
    
    # Initialize generator
    project_id = "dvvkusmi"
    api_token = "skc5ZCFCJ5o6xkoen6m3IidL61XifaoOHPYzcYBLFn2GIO3xxUAuSdfVTmyP8lYFTNo0e0MUvfyPNwNuj60pWcnm7XBQVIWH6bD47MAQ5KQBV0JnYReovwvIoXnuPvTYoEvRJFXlkWzs78zkD99cNL0DDWXTEBnStg2b6hmLmZDvQGoZTaNy"
    
    generator = STARTemplateGenerator(project_id, api_token)
    
    # Get templates from Sanity
    templates = generator.get_sanity_templates()
    
    if not templates:
        print("❌ No templates found in Sanity")
        return
    
    print(f"📋 Found {len(templates)} templates in Sanity")
    
    # Generate template files for each template
    generated_files = []
    for template in templates:
        try:
            template_file = generator.generate_template_files(template)
            generated_files.append(template_file)
            print(f"✅ Generated: {os.path.basename(template_file)}")
        except Exception as e:
            print(f"❌ Failed to generate template {template.get('name', 'Unknown')}: {e}")
    
    print(f"\n🎉 Generated {len(generated_files)} template files!")
    print("=" * 50)
    print("📁 Template files are ready for STAR integration:")
    for file in generated_files:
        print(f"   - {file}")
    
    print("\n🚀 Next steps:")
    print("1. Install templates using OASIS template system")
    print("2. Use STAR.LightAsync() with template IDs")
    print("3. Generate actual dApps from templates")
    
    return generator

if __name__ == "__main__":
    demo_star_template_generation() 