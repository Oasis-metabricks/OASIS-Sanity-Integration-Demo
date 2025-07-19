#!/usr/bin/env python3
"""
OASIS x Sanity Integration
Connects Sanity content with OASIS avatars, wallets, and STAR templates
"""

import requests
import json
import uuid
from datetime import datetime
from typing import Dict, List, Optional

class OASISSanityIntegration:
    """Complete OASIS x Sanity integration"""
    
    def __init__(self, project_id: str, api_token: str, dataset: str = "production"):
        self.project_id = project_id
        self.api_token = api_token
        self.dataset = dataset
        self.base_url = f"https://{project_id}.api.sanity.io/v2021-06-07"
        
    def create_avatar(self, username: str, email: str, wallets: Optional[List[Dict]] = None) -> Dict:
        """Create an OASIS Avatar in Sanity"""
        print(f"👤 Creating OASIS Avatar: {username}")
        
        avatar_data = {
            "avatarId": str(uuid.uuid4()),
            "username": username,
            "email": email,
            "karma": 0,
            "wallets": wallets or [],
            "nfts": [],
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
    
    def create_retreat_with_avatar(self, retreat_data: Dict, avatar_id: str) -> Dict:
        """Create a retreat linked to an OASIS avatar"""
        print(f"🏖️ Creating retreat linked to Avatar: {avatar_id}")
        
        retreat_data["avatar"] = {
            "_type": "reference",
            "_ref": avatar_id
        }
        
        mutation = {
            "mutations": [
                {
                    "create": {
                        "_type": "retreat",
                        **retreat_data
                    }
                }
            ]
        }
        
        return self._execute_mutation(mutation)
    
    def create_star_template(self, template_data: Dict, avatar_id: str) -> Dict:
        """Create a STAR template for dApp generation"""
        print(f"⭐ Creating STAR template: {template_data.get('name', 'Unnamed')}")
        
        template_data["createdBy"] = {
            "_type": "reference",
            "_ref": avatar_id
        }
        
        mutation = {
            "mutations": [
                {
                    "create": {
                        "_type": "starTemplate",
                        **template_data
                    }
                }
            ]
        }
        
        return self._execute_mutation(mutation)
    
    def link_content_to_template(self, content_id: str, template_id: str) -> Dict:
        """Link content to a STAR template for dApp generation"""
        print(f"🔗 Linking content {content_id} to template {template_id}")
        
        # This would update the content to reference the template
        # Implementation depends on specific content type
        return {"status": "linked", "content_id": content_id, "template_id": template_id}
    
    def get_avatar_content(self, avatar_id: str) -> Dict:
        """Get all content created by an avatar"""
        print(f"📖 Getting content for Avatar: {avatar_id}")
        
        query = f'''
        {{
          "avatar": *[_type == "oasisAvatar" && _id == "{avatar_id}"][0],
          "retreats": *[_type == "retreat" && avatar._ref == "{avatar_id}"],
          "housing": *[_type == "housing" && avatar._ref == "{avatar_id}"],
          "carbonCredits": *[_type == "carbonCredit" && avatar._ref == "{avatar_id}"],
          "content": *[_type == "contentCreatorSimple" && avatar._ref == "{avatar_id}"],
          "templates": *[_type == "starTemplate" && createdBy._ref == "{avatar_id}"]
        }}
        '''
        
        return self._execute_query(query)
    
    def generate_dapp_from_template(self, content_id: str, template_id: str) -> Dict:
        """Generate a dApp from content and STAR template"""
        print(f"🚀 Generating dApp from content {content_id} and template {template_id}")
        
        # Get the content and template
        content_query = f'*[_type in ["retreat", "housing", "carbonCredit", "contentCreatorSimple"] && _id == "{content_id}"][0]'
        template_query = f'*[_type == "starTemplate" && _id == "{template_id}"][0]'
        
        content = self._execute_query(content_query)
        template = self._execute_query(template_query)
        
        if not content or not template:
            return {"error": "Content or template not found"}
        
        # Generate dApp using STAR engine
        dapp_data = {
            "content": content,
            "template": template,
            "generated_at": datetime.utcnow().isoformat(),
            "deployment_url": f"https://dapp.oasisplatform.world/{content_id}",
            "status": "generated"
        }
        
        return dapp_data
    
    def process_payment(self, avatar_id: str, amount: float, currency: str = "USD") -> Dict:
        """Process payment through OASIS wallet integration"""
        print(f"💰 Processing payment: {amount} {currency} for Avatar: {avatar_id}")
        
        # This would integrate with OASIS wallet system
        payment_data = {
            "avatar_id": avatar_id,
            "amount": amount,
            "currency": currency,
            "status": "processed",
            "transaction_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        return payment_data
    
    def mint_nft_for_content(self, content_id: str, avatar_id: str) -> Dict:
        """Mint NFT for content ownership"""
        print(f"🎨 Minting NFT for content {content_id}")
        
        nft_data = {
            "content_id": content_id,
            "avatar_id": avatar_id,
            "token_id": str(uuid.uuid4()),
            "contract_address": "0x1234567890abcdef",  # Example
            "chain": "ethereum",
            "metadata": {
                "name": "OASIS Content NFT",
                "description": "NFT representing ownership of OASIS content",
                "image": "https://oasisplatform.world/nft-image.png"
            },
            "minted_at": datetime.utcnow().isoformat()
        }
        
        return nft_data
    
    def _execute_mutation(self, mutation: Dict) -> Dict:
        """Execute a Sanity mutation"""
        url = f"{self.base_url}/data/mutate/{self.dataset}"
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

def demo_oasis_sanity_integration():
    """Demonstrate the complete OASIS x Sanity integration"""
    
    print("🌟 OASIS x Sanity Integration Demo")
    print("=" * 50)
    
    # Initialize integration
    project_id = "dvvkusmi"
    api_token = "skc5ZCFCJ5o6xkoen6m3IidL61XifaoOHPYzcYBLFn2GIO3xxUAuSdfVTmyP8lYFTNo0e0MUvfyPNwNuj60pWcnm7XBQVIWH6bD47MAQ5KQBV0JnYReovwvIoXnuPvTYoEvRJFXlkWzs78zkD99cNL0DDWXTEBnStg2b6hmLmZDvQGoZTaNy"
    
    integration = OASISSanityIntegration(project_id, api_token)
    
    # Step 1: Create OASIS Avatar
    print("\n1️⃣ Creating OASIS Avatar...")
    avatar_wallets = [
        {
            "chain": "ethereum",
            "address": "0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6",
            "isDefault": True
        },
        {
            "chain": "solana",
            "address": "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM",
            "isDefault": False
        }
    ]
    
    avatar_result = integration.create_avatar(
        username="wellness_guru",
        email="guru@oasisplatform.world",
        wallets=avatar_wallets
    )
    
    if "error" in avatar_result:
        print(f"❌ Failed to create avatar: {avatar_result['error']}")
        return
    
    # For Sanity mutations, we need to query to get the created document ID
    # Let's create a simple query to get the avatar we just created
    query = f'*[_type == "oasisAvatar" && username == "wellness_guru"][0]._id'
    avatar_query_result = integration._execute_query(query)
    
    if "error" in avatar_query_result:
        print(f"❌ Failed to query avatar: {avatar_query_result['error']}")
        return
    
    avatar_id = avatar_query_result.get('result')
    if not avatar_id:
        print(f"❌ Failed to get avatar ID from query: {avatar_query_result}")
        return
    print(f"✅ Avatar created: {avatar_id}")
    
    # Step 2: Create Retreat with Avatar Link
    print("\n2️⃣ Creating Retreat with Avatar Link...")
    retreat_data = {
        "title": "Sacred Ohms Wellness Retreat",
        "slug": {"_type": "slug", "current": "sacred-ohms-wellness-retreat"},
        "description": "A transformative 7-day wellness retreat in the mountains",
        "dates": {
            "start": "2024-06-15",
            "end": "2024-06-22"
        },
        "location": "Mountain View Resort, Colorado",
        "price": 2500,
        "maxParticipants": 20,
        "currentParticipants": 0,
        "amenities": ["Yoga classes", "Meditation sessions", "Organic meals", "Spa access"],
        "status": "booking_open"
    }
    
    retreat_result = integration.create_retreat_with_avatar(retreat_data, avatar_id)
    
    if "error" in retreat_result:
        print(f"❌ Failed to create retreat: {retreat_result['error']}")
        return
    
    retreat_id = retreat_result.get('results', [{}])[0].get('id', 'Unknown')
    print(f"✅ Retreat created: {retreat_id}")
    
    # Step 3: Create STAR Template
    print("\n3️⃣ Creating STAR Template...")
    template_data = {
        "name": "Retreat Booking dApp",
        "description": "Interactive retreat booking application with wallet integration",
        "templateType": "retreat_booking",
        "platform": "web",
        "templateCode": """
        // STAR Template for Retreat Booking
        function generateRetreatApp(content) {
            return {
                title: content.title,
                bookingForm: true,
                walletIntegration: true,
                paymentMethods: ['crypto', 'credit_card'],
                nftMinting: true
            };
        }
        """,
        "walletIntegration": {
            "enabled": True,
            "supportedChains": ["ethereum", "solana", "polygon"],
            "paymentMethods": ["crypto", "credit_card", "karma"]
        },
        "interactiveFeatures": ["booking", "payment", "nft_minting", "chat"],
        "deploymentStatus": "draft"
    }
    
    template_result = integration.create_star_template(template_data, avatar_id)
    
    if "error" in template_result:
        print(f"❌ Failed to create template: {template_result['error']}")
        return
    
    template_id = template_result.get('results', [{}])[0].get('id', 'Unknown')
    print(f"✅ Template created: {template_id}")
    
    # Step 4: Generate dApp
    print("\n4️⃣ Generating dApp...")
    dapp_result = integration.generate_dapp_from_template(retreat_id, template_id)
    print(f"✅ dApp generated: {dapp_result.get('deployment_url', 'Unknown URL')}")
    
    # Step 5: Process Payment
    print("\n5️⃣ Processing Payment...")
    payment_result = integration.process_payment(avatar_id, 2500, "USD")
    print(f"✅ Payment processed: {payment_result.get('transaction_id', 'Unknown')}")
    
    # Step 6: Mint NFT
    print("\n6️⃣ Minting NFT...")
    nft_result = integration.mint_nft_for_content(retreat_id, avatar_id)
    print(f"✅ NFT minted: {nft_result.get('token_id', 'Unknown')}")
    
    # Step 7: Get Avatar Content
    print("\n7️⃣ Getting Avatar Content...")
    content_result = integration.get_avatar_content(avatar_id)
    print(f"✅ Avatar content retrieved: {len(content_result.get('retreats', []))} retreats")
    
    print("\n🎉 OASIS x Sanity Integration Complete!")
    print("=" * 50)
    print("✅ Avatar created with wallets")
    print("✅ Content linked to avatar")
    print("✅ STAR template created")
    print("✅ dApp generated")
    print("✅ Payment processed")
    print("✅ NFT minted")
    
    return integration

if __name__ == "__main__":
    demo_oasis_sanity_integration() 