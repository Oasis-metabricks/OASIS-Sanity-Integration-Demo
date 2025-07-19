# 🎯 OASIS x Sanity Integration Demo Guide

This guide walks you through the complete OASIS x Sanity integration, from avatar creation to dApp generation.

## 🚀 Quick Demo Overview

**What you'll see:**
1. **MagicMax Avatar** - A demo avatar with 1000 karma
2. **Content Creation** - Retreat booking content
3. **STAR Templates** - dApp generation templates
4. **dApp Generation** - Complete Blazor applications
5. **NFT Integration** - Content ownership and monetization

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- Git
- Basic understanding of blockchain concepts

## 🎭 Demo: MagicMax Avatar

### **Avatar Details**
- **Username**: MagicMax
- **Email**: max.gershfield1@gmail.com
- **Karma**: 1000
- **Bio**: "a man on a mission to build OASIS"
- **Solana Wallet**: 85ArqfA2fy8spGcMGsSW7cbEJAWj26vewmmoG2bwkgT9
- **NFT**: MagicMax OASIS Avatar NFT

### **View the Avatar**
1. Go to: https://oasis-avatar.sanity.studio
2. Click "OASIS Avatar" in the left sidebar
3. Find "MagicMax" in the list
4. Click to view details

## 🔧 Step-by-Step Demo

### **Step 1: Explore Sanity Studio**

```bash
# Start Sanity Studio
cd sanity-studio
npm run dev
```

**What to explore:**
- **OASIS Avatar**: View MagicMax and other avatars
- **Retreat**: See retreat booking content
- **STAR Template**: Check dApp generation templates
- **Housing**: Property listing content
- **Carbon Credit**: Environmental asset content

### **Step 2: Create Your Own Avatar**

```bash
# Run the avatar creation script
python3 scripts/create_magicmax_avatar.py
```

**Or create manually in Sanity Studio:**
1. Click "OASIS Avatar" → "Create new"
2. Fill in your details
3. Add wallet addresses
4. Set karma level
5. Click "Publish"

### **Step 3: Generate dApps**

```bash
# Generate dApps from content and templates
python3 scripts/star_integration.py
```

**What happens:**
1. Fetches content from Sanity
2. Matches with STAR templates
3. Generates complete dApp projects
4. Creates Blazor applications

### **Step 4: Build Projects**

```bash
# Build and prepare dApps for deployment
python3 scripts/build_star_projects.py
```

**Output:**
- Complete Blazor project files
- Wallet integration code
- NFT minting functionality
- Deployment scripts

## 🎨 Demo Content Examples

### **Retreat Booking dApp**
```json
{
  "title": "Sacred Ohms Wellness Retreat",
  "description": "A transformative 7-day wellness retreat",
  "price": 2500,
  "location": "Mountain View Resort, Colorado",
  "avatar": "MagicMax",
  "walletIntegration": true,
  "nftMinting": true
}
```

### **Generated dApp Features**
- **Booking System**: Interactive retreat booking
- **Wallet Integration**: Crypto payments
- **NFT Minting**: Retreat ownership tokens
- **Multi-Chain**: Solana, Ethereum, Polygon support

## 🔍 Code Examples

### **Avatar Creation**
```python
# Create OASIS Avatar
avatar_data = {
    "avatarId": "magicmax_aa334bc1",
    "username": "MagicMax",
    "email": "max.gershfield1@gmail.com",
    "karma": 1000,
    "wallets": [{"chain": "solana", "address": "85ArqfA2fy8spGcMGsSW7cbEJAWj26vewmmoG2bwkgT9"}],
    "nfts": [magicmax_nft],
    "bio": "a man on a mission to build OASIS"
}
```

### **STAR Template Generation**
```python
# Generate dApp from template
def create_star_project(template_data, content_data):
    project_name = f"{template_data['name']}_{content_data['id']}"
    # Creates complete Blazor project structure
    # Includes wallet integration and NFT features
    return project_structure
```

### **NFT Creation**
```python
# Create NFT for content
nft_data = {
    "tokenId": "magicmax_nft_aa334bc1",
    "contractAddress": "0x1234567890abcdef",
    "chain": "solana",
    "metadata": {
        "name": "MagicMax OASIS Avatar NFT",
        "attributes": [
            {"trait_type": "Avatar Type", "value": "OASIS Pioneer"},
            {"trait_type": "Karma Level", "value": "1000"}
        ]
    }
}
```

## 🌐 Live Demo URLs

### **Sanity Studio**
- **URL**: https://oasis-avatar.sanity.studio
- **Features**: Content management, avatar creation, template management

### **Generated dApps**
- **Retreat Booking**: https://dapp.oasisplatform.world/retreat-booking
- **Housing Marketplace**: https://dapp.oasisplatform.world/housing
- **Carbon Trading**: https://dapp.oasisplatform.world/carbon

## 📊 Demo Metrics

### **Current Status**
- ✅ **Avatars Created**: 10+ (including MagicMax)
- ✅ **Content Items**: 3+ retreats, housing, carbon credits
- ✅ **STAR Templates**: 1+ dApp templates
- ✅ **Generated Projects**: 3+ Blazor applications
- ✅ **NFTs Minted**: 1+ MagicMax avatar NFT

### **Blockchain Support**
- **Solana**: 85ArqfA2fy8spGcMGsSW7cbEJAWj26vewmmoG2bwkgT9
- **Ethereum**: 0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6
- **Polygon**: Ready for integration
- **Arbitrum**: Ready for integration
- **Holochain**: Ready for integration

## 🎯 Key Demo Points

### **1. No-Code dApp Creation**
- Content creators can build dApps without coding
- Templates handle the technical complexity
- Focus on content, not blockchain development

### **2. Multi-Chain Support**
- One avatar works across all blockchains
- Content can be deployed to any network
- Users can pay with their preferred cryptocurrency

### **3. NFT Monetization**
- Content becomes ownable NFTs
- Creators earn from secondary sales
- New revenue streams for content

### **4. Unified Identity**
- One avatar across all platforms
- Karma system for reputation
- Consistent user experience

## 🔧 Troubleshooting

### **Common Issues**

**Sanity Studio not loading:**
```bash
# Check if running on correct port
curl http://localhost:3333
```

**Python script errors:**
```bash
# Install dependencies
pip install -r scripts/requirements.txt
```

**Avatar not found:**
```bash
# List all avatars
python3 scripts/list_avatars.py
```

### **Debug Mode**
```bash
# Enable debug logging
export DEBUG=1
python3 scripts/oasis_sanity_integration.py
```

## 📈 Next Steps

### **For Developers**
1. **Extend Templates**: Create more dApp types
2. **Add Blockchains**: Support more networks
3. **Enhance UI**: Improve user interfaces
4. **Optimize Performance**: Faster generation

### **For Content Creators**
1. **Create Content**: Add more retreats, housing, etc.
2. **Customize Templates**: Modify dApp appearance
3. **Monetize Content**: Set up NFT sales
4. **Engage Community**: Build user base

### **For Businesses**
1. **Deploy dApps**: Go live with generated applications
2. **Scale Operations**: Handle more users
3. **Add Features**: Advanced functionality
4. **Market Integration**: Connect to existing systems

## 🎉 Demo Success Criteria

**You've successfully demonstrated the integration when:**
- ✅ Avatar is created in Sanity
- ✅ Content is linked to avatar
- ✅ dApp is generated from template
- ✅ Project builds successfully
- ✅ NFT is minted for content
- ✅ Wallet integration works

**Congratulations! You've built a complete Web3 content-to-dApp pipeline! 🚀** 