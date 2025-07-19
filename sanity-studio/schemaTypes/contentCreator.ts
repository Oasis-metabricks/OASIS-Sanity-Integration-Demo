export default {
  name: 'contentCreator',
  title: 'Content Creator',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Content Title',
      type: 'string',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96,
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'contentType',
      title: 'Content Type',
      type: 'string',
      options: {
        list: [
          {title: 'Blog Post', value: 'blog_post'},
          {title: 'Article', value: 'article'},
          {title: 'Tutorial', value: 'tutorial'},
          {title: 'Review', value: 'review'},
          {title: 'Interview', value: 'interview'},
          {title: 'Case Study', value: 'case_study'},
          {title: 'News', value: 'news'},
          {title: 'Opinion', value: 'opinion'}
        ]
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'avatarId',
      title: 'OASIS Avatar ID',
      type: 'string',
      description: 'The OASIS avatar that created this content',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'avatarWallet',
      title: 'Avatar Wallet Address',
      type: 'string',
      description: 'Wallet address for content monetization and tips'
    },
    {
      name: 'excerpt',
      title: 'Excerpt',
      type: 'text',
      rows: 3,
      description: 'Brief summary of the content'
    },
    {
      name: 'body',
      title: 'Body',
      type: 'array',
      of: [
        {
          type: 'block',
          styles: [
            {title: 'Normal', value: 'normal'},
            {title: 'H1', value: 'h1'},
            {title: 'H2', value: 'h2'},
            {title: 'H3', value: 'h3'},
            {title: 'Quote', value: 'blockquote'}
          ],
          marks: {
            decorators: [
              {title: 'Strong', value: 'strong'},
              {title: 'Emphasis', value: 'em'},
              {title: 'Code', value: 'code'}
            ],
            annotations: [
              {
                title: 'URL',
                name: 'link',
                type: 'object',
                fields: [
                  {
                    title: 'URL',
                    name: 'href',
                    type: 'url'
                  }
                ]
              }
            ]
          }
        },
        {
          type: 'image',
          options: {
            hotspot: true
          }
        },
        {
          type: 'text',
          title: 'Code Block',
          rows: 10
        }
      ]
    },
    {
      name: 'featuredImage',
      title: 'Featured Image',
      type: 'image',
      options: {
        hotspot: true
      }
    },
    {
      name: 'category',
      title: 'Category',
      type: 'string',
      options: {
        list: [
          {title: 'Technology', value: 'technology'},
          {title: 'Web3', value: 'web3'},
          {title: 'Blockchain', value: 'blockchain'},
          {title: 'Sustainability', value: 'sustainability'},
          {title: 'Wellness', value: 'wellness'},
          {title: 'Business', value: 'business'},
          {title: 'Lifestyle', value: 'lifestyle'},
          {title: 'Education', value: 'education'},
          {title: 'Entertainment', value: 'entertainment'},
          {title: 'Other', value: 'other'}
        ]
      }
    },
    {
      name: 'tags',
      title: 'Tags',
      type: 'array',
      of: [{type: 'string'}]
    },
    {
      name: 'monetization',
      title: 'Monetization',
      type: 'object',
      fields: [
        {
          name: 'isPremium',
          title: 'Premium Content',
          type: 'boolean',
          initialValue: false
        },
        {
          name: 'price',
          title: 'Price (USD)',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'cryptoPrice',
          title: 'Crypto Price',
          type: 'object',
          fields: [
            {
              name: 'ethereum',
              title: 'Ethereum (ETH)',
              type: 'number'
            },
            {
              name: 'solana',
              title: 'Solana (SOL)',
              type: 'number'
            },
            {
              name: 'oasisToken',
              title: 'OASIS Token',
              type: 'number'
            }
          ]
        },
        {
          name: 'allowTips',
          title: 'Allow Tips',
          type: 'boolean',
          initialValue: true
        },
        {
          name: 'minTipAmount',
          title: 'Minimum Tip Amount (USD)',
          type: 'number',
          initialValue: 1
        },
        {
          name: 'nftCollection',
          title: 'NFT Collection',
          type: 'object',
          fields: [
            {
              name: 'contractAddress',
              title: 'Contract Address',
              type: 'string'
            },
            {
              name: 'chain',
              title: 'Blockchain',
              type: 'string',
              options: {
                list: [
                  {title: 'Ethereum', value: 'ethereum'},
                  {title: 'Solana', value: 'solana'},
                  {title: 'Polygon', value: 'polygon'},
                  {title: 'Arbitrum', value: 'arbitrum'}
                ]
              }
            },
            {
              name: 'mintPrice',
              title: 'Mint Price',
              type: 'number'
            }
          ]
        }
      ]
    },
    {
      name: 'engagement',
      title: 'Engagement Metrics',
      type: 'object',
      fields: [
        {
          name: 'views',
          title: 'Views',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'likes',
          title: 'Likes',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'shares',
          title: 'Shares',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'comments',
          title: 'Comments',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'tipsReceived',
          title: 'Tips Received (USD)',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'nftsMinted',
          title: 'NFTs Minted',
          type: 'number',
          initialValue: 0
        }
      ]
    },
    {
      name: 'collaboration',
      title: 'Collaboration',
      type: 'object',
      fields: [
        {
          name: 'collaborators',
          title: 'Collaborators',
          type: 'array',
          of: [{
            type: 'object',
            fields: [
              {
                name: 'avatarId',
                title: 'OASIS Avatar ID',
                type: 'string'
              },
              {
                name: 'role',
                title: 'Role',
                type: 'string'
              },
              {
                name: 'contribution',
                title: 'Contribution (%)',
                type: 'number'
              }
            ]
          }]
        },
        {
          name: 'revenueSharing',
          title: 'Revenue Sharing',
          type: 'boolean',
          initialValue: false
        }
      ]
    },
    {
      name: 'seo',
      title: 'SEO',
      type: 'object',
      fields: [
        {
          name: 'metaTitle',
          title: 'Meta Title',
          type: 'string'
        },
        {
          name: 'metaDescription',
          title: 'Meta Description',
          type: 'text',
          rows: 2
        },
        {
          name: 'keywords',
          title: 'Keywords',
          type: 'array',
          of: [{type: 'string'}]
        }
      ]
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          {title: 'Draft', value: 'draft'},
          {title: 'Review', value: 'review'},
          {title: 'Published', value: 'published'},
          {title: 'Archived', value: 'archived'},
          {title: 'Deleted', value: 'deleted'}
        ]
      },
      initialValue: 'draft'
    },
    {
      name: 'publishedAt',
      title: 'Published at',
      type: 'datetime'
    },
    {
      name: 'updatedAt',
      title: 'Updated at',
      type: 'datetime'
    }
  ],
  preview: {
    select: {
      title: 'title',
      avatarId: 'avatarId',
      contentType: 'contentType',
      status: 'status',
      views: 'engagement.views'
    },
    prepare(selection: any) {
      const {title, avatarId, contentType, status, views} = selection
      return {
        title: title,
        subtitle: `Avatar: ${avatarId} | Type: ${contentType} | Views: ${views || 0} | Status: ${status}`
      }
    }
  }
} 