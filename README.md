<<<<<<< HEAD
# 🌟 OASIS x Sanity Integration Demo

**A complete integration between OASIS (Web3 Universal Operating System) and Sanity CMS for content-driven dApp generation.**

## 🎯 What We Built

This project demonstrates a **complete pipeline** from content creation in Sanity CMS to live dApp generation using OASIS's STAR engine. Content creators can now build decentralized applications without writing code.

### **Key Features**
- ✅ **OASIS Avatar System** - Digital identities with multi-chain wallets
- ✅ **Content Management** - Sanity CMS with OASIS schemas
- ✅ **STAR Template Engine** - Generate dApps from templates
- ✅ **NFT Integration** - Content ownership and monetization
- ✅ **Cross-Chain Support** - Ethereum, Solana, Polygon, Arbitrum, Holochain
- ✅ **Live dApp Generation** - From content to deployed applications

## 🏗️ Architecture Overview

```
Content Creator → Sanity CMS → OASIS Avatar → STAR Templates → Live dApp
      ↓              ↓            ↓              ↓              ↓
   Blog Post    Content Mgmt   Digital ID    Code Gen     Deployed App
```

## 📁 Project Structure

```
OASIS-Sanity-Integration-Demo/
├── sanity-studio/                 # Sanity CMS with OASIS schemas
│   ├── schemaTypes/
│   │   ├── oasisAvatar.ts        # OASIS Avatar schema
│   │   ├── retreat.ts            # Content schema
│   │   └── starTemplate.ts       # STAR template schema
│   └── sanity.config.ts
├── scripts/
│   ├── oasis_sanity_integration.py    # Main integration script
│   ├── star_template_generator.py     # Template generation
│   ├── star_integration.py            # STAR project creation
│   ├── build_star_projects.py         # Build and deploy
│   └── create_magicmax_avatar.py      # Avatar creation demo
├── generated_templates/           # Generated OAPP templates
├── star_projects/                # Generated dApp projects
└── docs/                         # Documentation
```

## 🚀 Quick Start

### 1. **Setup Sanity Studio**
```bash
cd sanity-studio
npm install
npm run dev
```
Access at: https://oasis-avatar.sanity.studio

### 2. **Create OASIS Avatar**
```bash
python3 scripts/create_magicmax_avatar.py
```

### 3. **Generate dApps**
```bash
python3 scripts/star_integration.py
```

### 4. **Build and Deploy**
```bash
python3 scripts/build_star_projects.py
```

## 🎭 Demo: MagicMax Avatar

We created a demo avatar called **MagicMax** with:
- **Username**: MagicMax
- **Email**: max.gershfield1@gmail.com
- **Karma**: 1000
- **Bio**: "a man on a mission to build OASIS"
- **Solana Wallet**: 85ArqfA2fy8spGcMGsSW7cbEJAWj26vewmmoG2bwkgT9
- **NFT**: MagicMax OASIS Avatar NFT

## 🔧 Technical Implementation

### **OASIS Avatar Schema**
```typescript
{
  name: 'oasisAvatar',
  title: 'OASIS Avatar',
  fields: [
    {name: 'avatarId', title: 'Avatar ID', type: 'string'},
    {name: 'username', title: 'Username', type: 'string'},
    {name: 'karma', title: 'Karma Level', type: 'number'},
    {name: 'wallets', title: 'Wallets', type: 'array'}, // Multi-chain
    {name: 'nfts', title: 'NFTs', type: 'array'}
  ]
}
```

### **STAR Template Generation**
```python
# Converts Sanity templates to OAPP template files
def generate_template_files(self, template_data: Dict) -> str:
    # Creates complete Blazor project structure
    # Generates .oapptemplate files for STAR engine
    # Includes wallet integration and NFT minting
```

### **dApp Generation Pipeline**
```python
# 1. Fetch content from Sanity
content = self._execute_query(content_query)

# 2. Match with STAR templates
template = self._execute_query(template_query)

# 3. Generate complete dApp project
project = self.create_star_project(template, content)

# 4. Build and deploy
self.build_project(project)
```

## 🌐 Live Demo

### **Sanity Studio**
- **URL**: https://oasis-avatar.sanity.studio
- **Features**: Create avatars, content, and STAR templates
- **OASIS Integration**: Full avatar and wallet management

### **Generated dApps**
- **Retreat Booking dApp**: Complete booking application
- **Housing Marketplace**: Property listing and purchase
- **Carbon Credit Trading**: Environmental asset trading
- **Content Monetization**: Creator economy platform

## 💡 Use Cases

### **1. Content Creator Platform**
```
Creator → Sanity → STAR → Live dApp
   ↓         ↓       ↓        ↓
Blog Post  Content  Template  Booking Site
```

### **2. Retreat Booking Business**
```
Retreat Owner → Sanity → STAR → Booking dApp
      ↓           ↓        ↓         ↓
Retreat Details  Content  Template  Live Site
```

### **3. NFT Marketplace**
```
Artist → Sanity → STAR → NFT dApp
  ↓        ↓       ↓        ↓
Artwork  Content  Template  Marketplace
```

## 🔗 OASIS Integration

### **Multi-Chain Wallet Support**
- **Ethereum**: 0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6
- **Solana**: 85ArqfA2fy8spGcMGsSW7cbEJAWj26vewmmoG2bwkgT9
- **Polygon**: 0x1234567890abcdef
- **Arbitrum**: 0xabcdef1234567890
- **Holochain**: hc://...

### **NFT System**
```python
nft_data = {
    "tokenId": "magicmax_nft_aa334bc1",
    "contractAddress": "0x1234567890abcdef",
    "chain": "solana",
    "metadata": {
        "name": "MagicMax OASIS Avatar NFT",
        "attributes": [
            {"trait_type": "Avatar Type", "value": "OASIS Pioneer"},
            {"trait_type": "Karma Level", "value": "1000"},
            {"trait_type": "Mission", "value": "Building OASIS"}
        ]
    }
}
```

## 🛠️ Development

### **Prerequisites**
- Python 3.8+
- Node.js 16+
- Sanity CLI
- OASIS Platform (for full deployment)

### **Installation**
```bash
# Clone repository
git clone <repository-url>
cd OASIS-Sanity-Integration-Demo

# Install dependencies
cd sanity-studio
npm install

# Setup Python environment
pip install requests
```

### **Configuration**
```bash
# Sanity configuration
cp sanity-studio/.env.example sanity-studio/.env
# Add your Sanity project ID and API token

# OASIS configuration
cp scripts/config.example.py scripts/config.py
# Add your OASIS API credentials
```

## 📊 Current Status

### **✅ Completed**
- OASIS Avatar schema integration
- Multi-chain wallet support
- STAR template generation
- dApp project creation
- NFT minting system
- Content linking to avatars

### **🚧 In Progress**
- OASIS NuGet package publishing
- Full STAR engine integration
- Live dApp deployment
- Wallet transaction processing

### **📋 Next Steps**
1. Publish OASIS packages to NuGet
2. Integrate STAR.LightAsync() calls
3. Add wallet transaction processing
4. Implement live dApp deployment
5. Add more blockchain providers

## 🎯 Value Proposition

### **For Content Creators**
- **No-Code dApp Creation**: Build dApps without blockchain knowledge
- **Direct Monetization**: Crypto payments and NFT ownership
- **Cross-Chain Compatibility**: Reach users on any blockchain

### **For Developers**
- **Template System**: Reusable dApp templates
- **OASIS Integration**: Access to 50+ blockchain providers
- **Unified Identity**: One avatar across all platforms

### **For Businesses**
- **Content-Driven Development**: Create dApps from existing content
- **Multi-Chain Reach**: Deploy across multiple blockchains
- **NFT Monetization**: New revenue streams through NFTs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the OASIS platform and follows the same licensing terms.

## 🌟 About OASIS

**OASIS** is a Web3 universal operating system that provides:
- **Programmable Digital Identities** (Avatars)
- **Cross-Chain Interoperability**
- **Modular Provider Architecture**
- **STAR Engine** for dApp generation
- **50+ Blockchain Provider Support**

---

**Built with ❤️ by the OASIS team**

*"A man on a mission to build OASIS" - MagicMax* 
=======
# OASIS-Sanity-Integration-Demo
>>>>>>> 03b99e0cec625e6ff8c52681fc23232e52ce6894
