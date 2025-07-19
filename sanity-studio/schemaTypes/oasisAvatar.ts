export default {
  name: 'oasisAvatar',
  title: 'OASIS Avatar',
  type: 'document',
  fields: [
    {
      name: 'avatarId',
      title: 'Avatar ID',
      type: 'string',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'username',
      title: 'Username',
      type: 'string',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'email',
      title: 'Email',
      type: 'string'
    },
    {
      name: 'karma',
      title: 'Karma Level',
      type: 'number',
      initialValue: 0
    },
    {
      name: 'wallets',
      title: 'Wallets',
      type: 'array',
      of: [{
        type: 'object',
        fields: [
          {
            name: 'chain',
            title: 'Blockchain',
            type: 'string',
            options: {
              list: [
                {title: 'Ethereum', value: 'ethereum'},
                {title: 'Solana', value: 'solana'},
                {title: 'Polygon', value: 'polygon'},
                {title: 'Arbitrum', value: 'arbitrum'},
                {title: 'Holochain', value: 'holochain'}
              ]
            }
          },
          {
            name: 'address',
            title: 'Wallet Address',
            type: 'string'
          },
          {
            name: 'isDefault',
            title: 'Default Wallet',
            type: 'boolean',
            initialValue: false
          }
        ]
      }]
    },
    {
      name: 'nfts',
      title: 'NFTs',
      type: 'array',
      of: [{
        type: 'object',
        fields: [
          {
            name: 'tokenId',
            title: 'Token ID',
            type: 'string'
          },
          {
            name: 'contractAddress',
            title: 'Contract Address',
            type: 'string'
          },
          {
            name: 'chain',
            title: 'Blockchain',
            type: 'string'
          },
          {
            name: 'metadata',
            title: 'Metadata',
            type: 'text'
          }
        ]
      }]
    },
    {
      name: 'profileImage',
      title: 'Profile Image',
      type: 'image',
      options: {
        hotspot: true
      }
    },
    {
      name: 'bio',
      title: 'Bio',
      type: 'text',
      rows: 3
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          {title: 'Active', value: 'active'},
          {title: 'Inactive', value: 'inactive'},
          {title: 'Suspended', value: 'suspended'}
        ]
      },
      initialValue: 'active'
    },
    {
      name: 'createdAt',
      title: 'Created At',
      type: 'datetime'
    },
    {
      name: 'lastActive',
      title: 'Last Active',
      type: 'datetime'
    }
  ],
  preview: {
    select: {
      title: 'username',
      avatarId: 'avatarId',
      karma: 'karma',
      status: 'status'
    },
    prepare(selection: any) {
      const {title, avatarId, karma, status} = selection
      return {
        title: title,
        subtitle: `ID: ${avatarId} | Karma: ${karma || 0} | Status: ${status}`
      }
    }
  }
} 