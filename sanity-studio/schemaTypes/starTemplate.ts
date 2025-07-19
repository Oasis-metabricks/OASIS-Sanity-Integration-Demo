export default {
  name: 'starTemplate',
  title: 'STAR Template',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Template Name',
      type: 'string',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 3
    },
    {
      name: 'templateType',
      title: 'Template Type',
      type: 'string',
      options: {
        list: [
          {title: 'Retreat Booking', value: 'retreat_booking'},
          {title: 'Housing Purchase', value: 'housing_purchase'},
          {title: 'Carbon Credit Trading', value: 'carbon_trading'},
          {title: 'Content Monetization', value: 'content_monetization'},
          {title: 'NFT Marketplace', value: 'nft_marketplace'},
          {title: 'DAO Governance', value: 'dao_governance'}
        ]
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'platform',
      title: 'Target Platform',
      type: 'string',
      options: {
        list: [
          {title: 'Web', value: 'web'},
          {title: 'Unity', value: 'unity'},
          {title: 'Mobile', value: 'mobile'},
          {title: 'Console', value: 'console'},
          {title: 'VR/AR', value: 'vr_ar'}
        ]
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'templateCode',
      title: 'Template Code',
      type: 'text',
      rows: 20,
      description: 'STAR template code for generating dApps'
    },
    {
      name: 'walletIntegration',
      title: 'Wallet Integration',
      type: 'object',
      fields: [
        {
          name: 'enabled',
          title: 'Enable Wallet Integration',
          type: 'boolean',
          initialValue: true
        },
        {
          name: 'supportedChains',
          title: 'Supported Blockchains',
          type: 'array',
          of: [{type: 'string'}],
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
          name: 'paymentMethods',
          title: 'Payment Methods',
          type: 'array',
          of: [{type: 'string'}],
          options: {
            list: [
              {title: 'Crypto', value: 'crypto'},
              {title: 'Credit Card', value: 'credit_card'},
              {title: 'Bank Transfer', value: 'bank_transfer'},
              {title: 'Karma', value: 'karma'}
            ]
          }
        }
      ]
    },
    {
      name: 'interactiveFeatures',
      title: 'Interactive Features',
      type: 'array',
      of: [{type: 'string'}],
      options: {
        list: [
          {title: 'Booking System', value: 'booking'},
          {title: 'Payment Processing', value: 'payment'},
          {title: 'NFT Minting', value: 'nft_minting'},
          {title: 'Voting System', value: 'voting'},
          {title: 'Chat/Messaging', value: 'chat'},
          {title: 'Real-time Updates', value: 'realtime'},
          {title: '3D Visualization', value: '3d_visualization'},
          {title: 'AR/VR Support', value: 'ar_vr'}
        ]
      }
    },
    {
      name: 'deploymentStatus',
      title: 'Deployment Status',
      type: 'string',
      options: {
        list: [
          {title: 'Draft', value: 'draft'},
          {title: 'Testing', value: 'testing'},
          {title: 'Deployed', value: 'deployed'},
          {title: 'Archived', value: 'archived'}
        ]
      },
      initialValue: 'draft'
    },
    {
      name: 'deployedUrl',
      title: 'Deployed URL',
      type: 'url',
      description: 'URL where the generated dApp is deployed'
    },
    {
      name: 'createdBy',
      title: 'Created By',
      type: 'reference',
      to: [{type: 'oasisAvatar'}]
    },
    {
      name: 'version',
      title: 'Version',
      type: 'string',
      initialValue: '1.0.0'
    },
    {
      name: 'tags',
      title: 'Tags',
      type: 'array',
      of: [{type: 'string'}]
    }
  ],
  preview: {
    select: {
      title: 'name',
      templateType: 'templateType',
      platform: 'platform',
      deploymentStatus: 'deploymentStatus'
    },
    prepare(selection: any) {
      const {title, templateType, platform, deploymentStatus} = selection
      return {
        title: title,
        subtitle: `${templateType} | ${platform} | ${deploymentStatus}`
      }
    }
  }
} 