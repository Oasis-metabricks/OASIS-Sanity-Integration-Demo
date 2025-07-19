#!/usr/bin/env python3
"""
Build and Run STAR Projects
Builds and runs the generated STAR projects
"""

import os
import subprocess
import json
import time
from typing import Dict, List, Optional

class STARProjectBuilder:
    """Builds and runs STAR projects"""
    
    def __init__(self):
        self.projects_dir = "star_projects"
        self.built_projects = []
    
    def build_all_projects(self) -> List[Dict]:
        """Build all generated STAR projects"""
        print("🔨 Building STAR projects...")
        
        if not os.path.exists(self.projects_dir):
            print("❌ No projects directory found")
            return []
        
        projects = []
        for project_name in os.listdir(self.projects_dir):
            project_path = os.path.join(self.projects_dir, project_name)
            
            if os.path.isdir(project_path):
                try:
                    result = self.build_project(project_path, project_name)
                    if result:
                        projects.append(result)
                except Exception as e:
                    print(f"❌ Failed to build {project_name}: {e}")
        
        self.built_projects = projects
        return projects
    
    def build_project(self, project_path: str, project_name: str) -> Optional[Dict]:
        """Build a single STAR project"""
        print(f"🔨 Building project: {project_name}")
        
        # Check if it's a valid .NET project
        csproj_files = [f for f in os.listdir(project_path) if f.endswith('.csproj')]
        if not csproj_files:
            print(f"❌ No .csproj file found in {project_name}")
            return None
        
        # Read project configuration
        config_file = os.path.join(project_path, "star-config.json")
        config = {}
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
        
        # Build the project
        try:
            # Restore packages
            print(f"   📦 Restoring packages...")
            restore_result = subprocess.run(
                ["dotnet", "restore"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if restore_result.returncode != 0:
                print(f"   ❌ Package restore failed: {restore_result.stderr}")
                return None
            
            # Build the project
            print(f"   🔨 Building project...")
            build_result = subprocess.run(
                ["dotnet", "build"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if build_result.returncode != 0:
                print(f"   ❌ Build failed: {build_result.stderr}")
                return None
            
            # Publish the project
            print(f"   📤 Publishing project...")
            publish_dir = os.path.join(project_path, "bin", "Release", "net8.0", "publish")
            
            publish_result = subprocess.run(
                ["dotnet", "publish", "-c", "Release"],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            
            if publish_result.returncode != 0:
                print(f"   ❌ Publish failed: {publish_result.stderr}")
                return None
            
            print(f"   ✅ Project built successfully")
            
            return {
                "project_name": project_name,
                "project_path": project_path,
                "publish_path": publish_dir,
                "config": config,
                "build_status": "success",
                "launch_command": f"dotnet run --project {project_path}"
            }
            
        except Exception as e:
            print(f"   ❌ Build error: {e}")
            return None
    
    def run_project(self, project_info: Dict) -> bool:
        """Run a built STAR project"""
        project_name = project_info['project_name']
        project_path = project_info['project_path']
        
        print(f"🚀 Running project: {project_name}")
        
        try:
            # Start the project in the background
            process = subprocess.Popen(
                ["dotnet", "run"],
                cwd=project_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a moment for the project to start
            time.sleep(3)
            
            if process.poll() is None:
                print(f"   ✅ Project started successfully (PID: {process.pid})")
                print(f"   🌐 Access at: https://localhost:5001")
                return True
            else:
                stdout, stderr = process.communicate()
                print(f"   ❌ Project failed to start: {stderr}")
                return False
                
        except Exception as e:
            print(f"   ❌ Failed to run project: {e}")
            return False
    
    def create_deployment_script(self, project_info: Dict) -> str:
        """Create a deployment script for the project"""
        project_name = project_info['project_name']
        project_path = project_info['project_path']
        
        script_content = f'''#!/bin/bash
# Deployment script for {project_name}

echo "🚀 Deploying {project_name}..."

# Build the project
cd "{project_path}"
dotnet restore
dotnet build -c Release
dotnet publish -c Release

# Create deployment package
deploy_dir="deploy_{project_name}"
mkdir -p $deploy_dir
cp -r bin/Release/net8.0/publish/* $deploy_dir/

# Create startup script
cat > $deploy_dir/start.sh << 'EOF'
#!/bin/bash
export ASPNETCORE_ENVIRONMENT=Production
export ASPNETCORE_URLS=http://0.0.0.0:5000
dotnet {project_name}.dll
EOF

chmod +x $deploy_dir/start.sh

echo "✅ {project_name} deployed to $deploy_dir"
echo "🚀 Run with: cd $deploy_dir && ./start.sh"
'''
        
        script_path = f"deploy_{project_name}.sh"
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        os.chmod(script_path, 0o755)
        return script_path
    
    def create_dockerfile(self, project_info: Dict) -> str:
        """Create a Dockerfile for the project"""
        project_name = project_info['project_name']
        
        dockerfile_content = f'''# Dockerfile for {project_name}
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["{project_name}.csproj", "./"]
RUN dotnet restore "./{project_name}.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "{project_name}.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "{project_name}.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "{project_name}.dll"]
'''
        
        dockerfile_path = os.path.join(project_info['project_path'], "Dockerfile")
        with open(dockerfile_path, 'w') as f:
            f.write(dockerfile_content)
        
        return dockerfile_path
    
    def generate_readme(self, project_info: Dict) -> str:
        """Generate a README for the project"""
        project_name = project_info['project_name']
        config = project_info['config']
        
        readme_content = f'''# {project_name}

This is a STAR-generated dApp created from Sanity content and templates.

## Project Details

- **Template**: {config.get('projectName', 'Unknown')}
- **Content Type**: {config.get('contentType', 'Unknown')}
- **Platform**: {config.get('platform', 'web')}
- **Generated**: {config.get('generatedAt', 'Unknown')}

## Features

- OASIS Avatar Integration
- Wallet Support: {', '.join(config.get('walletIntegration', {}).get('supportedChains', []))}
- Interactive Features: {', '.join(config.get('interactiveFeatures', []))}

## Quick Start

### Local Development
```bash
cd {project_info['project_path']}
dotnet restore
dotnet run
```

### Production Deployment
```bash
# Build for production
dotnet publish -c Release

# Run the published app
dotnet bin/Release/net8.0/publish/{project_name}.dll
```

### Docker Deployment
```bash
# Build Docker image
docker build -t {project_name.lower().replace(' ', '-')} .

# Run container
docker run -p 5000:80 {project_name.lower().replace(' ', '-')}
```

## OASIS Integration

This dApp integrates with the OASIS platform for:
- Avatar authentication
- Wallet transactions
- Content management
- Cross-chain interoperability

## Support

For support, visit the OASIS platform documentation.
'''
        
        readme_path = os.path.join(project_info['project_path'], "README.md")
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        return readme_path

def demo_star_project_building():
    """Demonstrate building and running STAR projects"""
    
    print("🌟 STAR Project Building Demo")
    print("=" * 50)
    
    builder = STARProjectBuilder()
    
    # Build all projects
    print("\n1️⃣ Building all STAR projects...")
    built_projects = builder.build_all_projects()
    
    if not built_projects:
        print("❌ No projects were built successfully")
        return
    
    print(f"✅ Built {len(built_projects)} projects successfully")
    
    # Create deployment artifacts
    print("\n2️⃣ Creating deployment artifacts...")
    for project in built_projects:
        try:
            # Create deployment script
            deploy_script = builder.create_deployment_script(project)
            print(f"   📜 Created deployment script: {deploy_script}")
            
            # Create Dockerfile
            dockerfile = builder.create_dockerfile(project)
            print(f"   🐳 Created Dockerfile: {dockerfile}")
            
            # Create README
            readme = builder.generate_readme(project)
            print(f"   📖 Created README: {readme}")
            
        except Exception as e:
            print(f"   ❌ Failed to create artifacts for {project['project_name']}: {e}")
    
    # Run a sample project (optional)
    print("\n3️⃣ Running sample project...")
    if built_projects:
        sample_project = built_projects[0]
        print(f"🚀 Running: {sample_project['project_name']}")
        
        # Note: In a real scenario, you might want to run this in a separate process
        # For demo purposes, we'll just show the command
        print(f"   Command: {sample_project['launch_command']}")
        print(f"   Access: https://localhost:5001")
    
    print(f"\n🎉 STAR Project Building Complete!")
    print("=" * 50)
    print(f"✅ Built {len(built_projects)} projects")
    print("✅ Created deployment scripts")
    print("✅ Created Dockerfiles")
    print("✅ Created READMEs")
    
    print("\n🚀 Next steps:")
    print("1. Run projects locally for testing")
    print("2. Deploy to production servers")
    print("3. Integrate with OASIS wallet system")
    print("4. Monitor and maintain dApps")
    
    return builder

if __name__ == "__main__":
    demo_star_project_building() 