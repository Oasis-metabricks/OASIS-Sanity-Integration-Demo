#!/usr/bin/env python3
"""
Create MagicMax OASIS Avatar
Custom avatar creation with NFT and profile image
"""

import requests
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional

class MagicMaxAvatarCreator:
    """Create MagicMax OASIS Avatar with custom details"""
    
    def __init__(self):
        self.project_id = "dvvkusmi"
        self.api_token = "skc5ZCFCJ5o6xkoen6m3IidL61XifaoOHPYzcYBLFn2GIO3xxUAuSdfVTmyP8lYFTNo0e0MUvfyPNwNuj60pWcnm7XBQVIWH6bD47MAQ5KQBV0JnYReovwvIoXnuPvTYoEvRJFXlkWzs78zkD99cNL0DDWXTEBnStg2b6hmLmZDvQGoZTaNy"
        self.base_url = f"https://{self.project_id}.api.sanity.io/v2021-06-07"
    
    def create_magicmax_avatar(self) -> Dict:
        """Create MagicMax avatar with all specified details"""
        print("🌟 Creating MagicMax OASIS Avatar...")
        
        # Generate avatar ID similar to the pattern you mentioned
        avatar_id = f"magicmax_{str(uuid.uuid4())[:8]}"
        
        # Create Solana wallet data
        solana_wallet = {
            "chain": "solana",
            "address": "85ArqfA2fy8spGcMGsSW7cbEJAWj26vewmmoG2bwkgT9",
            "isDefault": True
        }
        
        # Create NFT for MagicMax
        magicmax_nft = self._create_magicmax_nft()
        
        avatar_data = {
            "avatarId": avatar_id,
            "username": "MagicMax",
            "email": "max.gershfield1@gmail.com",
            "karma": 1000,
            "wallets": [solana_wallet],
            "nfts": [magicmax_nft],
            "bio": "a man on a mission to build OASIS",
            "status": "active",
            "createdAt": datetime.utcnow().isoformat(),
            "lastActive": datetime.utcnow().isoformat()
        }
        
        mutation = {
            "mutations": [
                {
                    "create": {
                        "_type": "oasisAvatar",
                        **avatar_data
                    }
                }
            ]
        }
        
        return self._execute_mutation(mutation)
    
    def _create_magicmax_nft(self) -> Dict:
        """Create NFT for MagicMax using OASIS NFT logic"""
        print("🎨 Creating MagicMax NFT...")
        
        nft_data = {
            "tokenId": f"magicmax_nft_{str(uuid.uuid4())[:8]}",
            "contractAddress": "0x1234567890abcdef",  # Example contract address
            "chain": "solana",
            "metadata": {
                "name": "MagicMax OASIS Avatar NFT",
                "description": "NFT representing MagicMax's digital identity in the OASIS platform",
                "image": "https://oasisplatform.world/nft-images/magicmax-avatar.png",
                "attributes": [
                    {
                        "trait_type": "Avatar Type",
                        "value": "OASIS Pioneer"
                    },
                    {
                        "trait_type": "Karma Level",
                        "value": "1000"
                    },
                    {
                        "trait_type": "Mission",
                        "value": "Building OASIS"
                    },
                    {
                        "trait_type": "Blockchain",
                        "value": "Solana"
                    }
                ],
                "external_url": "https://oasisplatform.world/avatars/magicmax",
                "animation_url": "https://oasisplatform.world/avatars/magicmax/3d-model.glb"
            },
            "minted_at": datetime.utcnow().isoformat(),
            "creator": "OASIS Platform",
            "royalty_percentage": 2.5
        }
        
        return nft_data
    
    def upload_profile_image(self, avatar_id: str, image_url: Optional[str] = None) -> Dict:
        """Upload profile image for the avatar"""
        print("📸 Handling profile image upload...")
        
        # For now, we'll use a placeholder image URL
        # In a full implementation, this would upload to IPFS or similar
        profile_image_url = image_url or "https://oasisplatform.world/avatars/magicmax/profile.jpg"
        
        mutation = {
            "mutations": [
                {
                    "patch": {
                        "id": avatar_id,
                        "set": {
                            "profileImage": {
                                "_type": "image",
                                "asset": {
                                    "_type": "reference",
                                    "_ref": profile_image_url
                                }
                            }
                        }
                    }
                }
            ]
        }
        
        return self._execute_mutation(mutation)
    
    def get_avatar_details(self, avatar_id: str) -> Dict:
        """Get complete avatar details"""
        if not avatar_id or avatar_id == 'Unknown':
            return {"error": "Invalid avatar ID"}
        query = f'*[_type == "oasisAvatar" && _id == "{avatar_id}"][0]'
        return self._execute_query(query)
    
    def _execute_mutation(self, mutation: Dict) -> Dict:
        """Execute a Sanity mutation"""
        url = f"{self.base_url}/data/mutate/production"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, headers=headers, json=mutation)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Mutation failed: {response.status_code}")
                return {"error": response.text}
        except Exception as e:
            print(f"❌ Error executing mutation: {e}")
            return {"error": str(e)}
    
    def _execute_query(self, query: str) -> Dict:
        """Execute a Sanity query"""
        url = f"{self.base_url}/data/query/production"
        params = {"query": query}
        headers = {
            "Authorization": f"Bearer {self.api_token}"
        }
        
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

def main():
    """Create MagicMax avatar"""
    creator = MagicMaxAvatarCreator()
    
    print("🌟 Creating MagicMax OASIS Avatar")
    print("=" * 50)
    
    # Create the avatar
    result = creator.create_magicmax_avatar()
    
    if "error" in result:
        print(f"❌ Failed to create avatar: {result['error']}")
        return
    
    avatar_id = result.get('results', [{}])[0].get('id', 'Unknown')
    print(f"✅ MagicMax avatar created successfully!")
    print(f"   Avatar ID: {avatar_id}")
    
    # Get avatar details
    avatar_details = creator.get_avatar_details(avatar_id)
    
    if avatar_details and 'result' in avatar_details and avatar_details['result']:
        avatar = avatar_details['result']
        print(f"\n🎉 MagicMax Avatar Details:")
        print(f"   ID: {avatar.get('avatarId', 'Unknown')}")
        print(f"   Username: {avatar.get('username', 'Unknown')}")
        print(f"   Email: {avatar.get('email', 'Unknown')}")
        print(f"   Karma: {avatar.get('karma', 0)}")
        print(f"   Bio: {avatar.get('bio', 'No bio')}")
        print(f"   Status: {avatar.get('status', 'Unknown')}")
        
        # Show wallets
        wallets = avatar.get('wallets', [])
        if wallets:
            print(f"   Wallets:")
            for wallet in wallets:
                print(f"     - {wallet.get('chain', 'Unknown')}: {wallet.get('address', 'Unknown')}")
        
        # Show NFTs
        nfts = avatar.get('nfts', [])
        if nfts:
            print(f"   NFTs:")
            for nft in nfts:
                print(f"     - {nft.get('metadata', {}).get('name', 'Unknown NFT')}")
                print(f"       Token ID: {nft.get('tokenId', 'Unknown')}")
                print(f"       Chain: {nft.get('chain', 'Unknown')}")
    else:
        print(f"\n📋 Avatar created with ID: {avatar_id}")
        print(f"   Username: MagicMax")
        print(f"   Email: max.gershfield1@gmail.com")
        print(f"   Karma: 1000")
        print(f"   Bio: a man on a mission to build OASIS")
        print(f"   Solana Wallet: 85ArqfA2fy8spGcMGsSW7cbEJAWj26vewmmoG2bwkgT9")
        print(f"   NFT: MagicMax OASIS Avatar NFT (Solana)")
    
    print(f"\n🌐 View your avatar:")
    print(f"   Sanity Studio: https://oasis-avatar.sanity.studio")
    print(f"   Avatar ID: {avatar_id}")
    
    print(f"\n💡 Next steps:")
    print(f"   1. Add more wallet addresses")
    print(f"   2. Create content linked to your avatar")
    print(f"   3. Generate dApps using STAR templates")
    print(f"   4. Mint more NFTs for your content")

if __name__ == "__main__":
    main() 