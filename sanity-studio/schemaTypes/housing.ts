export default {
  name: 'housing',
  title: 'Housing Project',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Project Title',
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
      name: 'description',
      title: 'Description',
      type: 'text',
      rows: 4,
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'avatarId',
      title: 'OASIS Avatar ID',
      type: 'string',
      description: 'The OASIS avatar that created this housing project',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'avatarWallet',
      title: 'Avatar Wallet Address',
      type: 'string',
      description: 'Wallet address for project funding and token distribution'
    },
    {
      name: 'projectType',
      title: 'Project Type',
      type: 'string',
      options: {
        list: [
          {title: 'Modular Home', value: 'modular'},
          {title: 'Tiny House', value: 'tiny_house'},
          {title: 'Co-housing Community', value: 'co_housing'},
          {title: 'Sustainable Village', value: 'sustainable_village'},
          {title: 'Off-grid Community', value: 'off_grid'}
        ]
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'location',
      title: 'Location',
      type: 'string',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'coordinates',
      title: 'Coordinates',
      type: 'object',
      fields: [
        {
          name: 'lat',
          title: 'Latitude',
          type: 'number'
        },
        {
          name: 'lng',
          title: 'Longitude',
          type: 'number'
        }
      ]
    },
    {
      name: 'totalUnits',
      title: 'Total Units',
      type: 'number',
      validation: (Rule: any) => Rule.required().min(1)
    },
    {
      name: 'availableUnits',
      title: 'Available Units',
      type: 'number',
      initialValue: 0
    },
    {
      name: 'unitPrice',
      title: 'Unit Price (USD)',
      type: 'number',
      validation: (Rule: any) => Rule.required().min(0)
    },
    {
      name: 'fractionalOwnership',
      title: 'Fractional Ownership',
      type: 'object',
      fields: [
        {
          name: 'enabled',
          title: 'Enable Fractional Ownership',
          type: 'boolean',
          initialValue: false
        },
        {
          name: 'minFraction',
          title: 'Minimum Fraction (%)',
          type: 'number',
          initialValue: 1
        },
        {
          name: 'tokenContract',
          title: 'Token Contract Address',
          type: 'string'
        },
        {
          name: 'totalTokens',
          title: 'Total Tokens',
          type: 'number'
        }
      ]
    },
    {
      name: 'supplyChain',
      title: 'Supply Chain',
      type: 'object',
      fields: [
        {
          name: 'materials',
          title: 'Materials',
          type: 'array',
          of: [{
            type: 'object',
            fields: [
              {
                name: 'name',
                title: 'Material Name',
                type: 'string'
              },
              {
                name: 'source',
                title: 'Source',
                type: 'string'
              },
              {
                name: 'sustainability',
                title: 'Sustainability Rating',
                type: 'number',
                validation: (Rule: any) => Rule.min(1).max(10)
              },
              {
                name: 'blockchainId',
                title: 'Blockchain ID',
                type: 'string',
                description: 'Unique identifier on blockchain for tracking'
              }
            ]
          }]
        },
        {
          name: 'suppliers',
          title: 'Suppliers',
          type: 'array',
          of: [{
            type: 'object',
            fields: [
              {
                name: 'name',
                title: 'Supplier Name',
                type: 'string'
              },
              {
                name: 'avatarId',
                title: 'OASIS Avatar ID',
                type: 'string'
              },
              {
                name: 'rating',
                title: 'Rating',
                type: 'number',
                validation: (Rule: any) => Rule.min(1).max(5)
              }
            ]
          }]
        }
      ]
    },
    {
      name: 'sustainability',
      title: 'Sustainability Features',
      type: 'object',
      fields: [
        {
          name: 'energyRating',
          title: 'Energy Rating',
          type: 'string',
          options: {
            list: [
              {title: 'A+', value: 'A_plus'},
              {title: 'A', value: 'A'},
              {title: 'B', value: 'B'},
              {title: 'C', value: 'C'},
              {title: 'D', value: 'D'},
              {title: 'E', value: 'E'},
              {title: 'F', value: 'F'},
              {title: 'G', value: 'G'}
            ]
          }
        },
        {
          name: 'renewableEnergy',
          title: 'Renewable Energy',
          type: 'boolean',
          initialValue: false
        },
        {
          name: 'waterRecycling',
          title: 'Water Recycling',
          type: 'boolean',
          initialValue: false
        },
        {
          name: 'carbonFootprint',
          title: 'Carbon Footprint (tons CO2)',
          type: 'number'
        }
      ]
    },
    {
      name: 'funding',
      title: 'Funding',
      type: 'object',
      fields: [
        {
          name: 'targetAmount',
          title: 'Target Amount (USD)',
          type: 'number'
        },
        {
          name: 'raisedAmount',
          title: 'Raised Amount (USD)',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'fundingType',
          title: 'Funding Type',
          type: 'string',
          options: {
            list: [
              {title: 'Crowdfunding', value: 'crowdfunding'},
              {title: 'DAO', value: 'dao'},
              {title: 'Traditional', value: 'traditional'},
              {title: 'Hybrid', value: 'hybrid'}
            ]
          }
        },
        {
          name: 'daoContract',
          title: 'DAO Contract Address',
          type: 'string'
        }
      ]
    },
    {
      name: 'images',
      title: 'Images',
      type: 'array',
      of: [{type: 'image'}],
      options: {
        hotspot: true
      }
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          {title: 'Planning', value: 'planning'},
          {title: 'Funding', value: 'funding'},
          {title: 'Construction', value: 'construction'},
          {title: 'Pre-sale', value: 'pre_sale'},
          {title: 'Available', value: 'available'},
          {title: 'Completed', value: 'completed'},
          {title: 'Cancelled', value: 'cancelled'}
        ]
      },
      initialValue: 'planning'
    },
    {
      name: 'tags',
      title: 'Tags',
      type: 'array',
      of: [{type: 'string'}]
    },
    {
      name: 'publishedAt',
      title: 'Published at',
      type: 'datetime'
    }
  ],
  preview: {
    select: {
      title: 'title',
      avatarId: 'avatarId',
      status: 'status',
      projectType: 'projectType'
    },
    prepare(selection: any) {
      const {title, avatarId, status, projectType} = selection
      return {
        title: title,
        subtitle: `Avatar: ${avatarId} | Type: ${projectType} | Status: ${status}`
      }
    }
  }
} 