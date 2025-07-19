export default {
  name: 'carbonCredit',
  title: 'Carbon Credit Project',
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
      description: 'The OASIS avatar that created this carbon credit project',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'avatarWallet',
      title: 'Avatar Wallet Address',
      type: 'string',
      description: 'Wallet address for carbon credit tokenization and trading'
    },
    {
      name: 'projectType',
      title: 'Project Type',
      type: 'string',
      options: {
        list: [
          {title: 'Reforestation', value: 'reforestation'},
          {title: 'Renewable Energy', value: 'renewable_energy'},
          {title: 'Ocean Conservation', value: 'ocean_conservation'},
          {title: 'Waste Management', value: 'waste_management'},
          {title: 'Sustainable Agriculture', value: 'sustainable_agriculture'},
          {title: 'Clean Technology', value: 'clean_technology'},
          {title: 'Forest Conservation', value: 'forest_conservation'},
          {title: 'Blue Carbon', value: 'blue_carbon'}
        ]
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'location',
      title: 'Project Location',
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
      name: 'certification',
      title: 'Certification',
      type: 'object',
      fields: [
        {
          name: 'standard',
          title: 'Certification Standard',
          type: 'string',
          options: {
            list: [
              {title: 'Gold Standard', value: 'gold_standard'},
              {title: 'Verified Carbon Standard (VCS)', value: 'vcs'},
              {title: 'Climate Action Reserve', value: 'climate_action_reserve'},
              {title: 'American Carbon Registry', value: 'american_carbon_registry'},
              {title: 'Plan Vivo', value: 'plan_vivo'},
              {title: 'OASIS Carbon Standard', value: 'oasis_standard'}
            ]
          }
        },
        {
          name: 'certificationId',
          title: 'Certification ID',
          type: 'string'
        },
        {
          name: 'certificationDate',
          title: 'Certification Date',
          type: 'date'
        },
        {
          name: 'validUntil',
          title: 'Valid Until',
          type: 'date'
        }
      ]
    },
    {
      name: 'carbonMetrics',
      title: 'Carbon Metrics',
      type: 'object',
      fields: [
        {
          name: 'totalCredits',
          title: 'Total Carbon Credits (tons CO2e)',
          type: 'number',
          validation: (Rule: any) => Rule.required().min(0)
        },
        {
          name: 'availableCredits',
          title: 'Available Credits (tons CO2e)',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'soldCredits',
          title: 'Sold Credits (tons CO2e)',
          type: 'number',
          initialValue: 0
        },
        {
          name: 'pricePerCredit',
          title: 'Price per Credit (USD)',
          type: 'number',
          validation: (Rule: any) => Rule.required().min(0)
        },
        {
          name: 'projectLifetime',
          title: 'Project Lifetime (years)',
          type: 'number'
        },
        {
          name: 'annualReduction',
          title: 'Annual CO2 Reduction (tons)',
          type: 'number'
        }
      ]
    },
    {
      name: 'tokenization',
      title: 'Tokenization',
      type: 'object',
      fields: [
        {
          name: 'enabled',
          title: 'Enable Tokenization',
          type: 'boolean',
          initialValue: false
        },
        {
          name: 'tokenContract',
          title: 'Token Contract Address',
          type: 'string'
        },
        {
          name: 'tokenSymbol',
          title: 'Token Symbol',
          type: 'string'
        },
        {
          name: 'tokensPerCredit',
          title: 'Tokens per Carbon Credit',
          type: 'number',
          initialValue: 1
        },
        {
          name: 'blockchain',
          title: 'Blockchain',
          type: 'string',
          options: {
            list: [
              {title: 'Ethereum', value: 'ethereum'},
              {title: 'Polygon', value: 'polygon'},
              {title: 'Solana', value: 'solana'},
              {title: 'Arbitrum', value: 'arbitrum'},
              {title: 'OASIS Chain', value: 'oasis_chain'}
            ]
          }
        },
        {
          name: 'tradingEnabled',
          title: 'Enable Trading',
          type: 'boolean',
          initialValue: false
        }
      ]
    },
    {
      name: 'environmentalImpact',
      title: 'Environmental Impact',
      type: 'object',
      fields: [
        {
          name: 'biodiversity',
          title: 'Biodiversity Impact',
          type: 'text',
          rows: 3
        },
        {
          name: 'waterConservation',
          title: 'Water Conservation (liters/year)',
          type: 'number'
        },
        {
          name: 'airQuality',
          title: 'Air Quality Improvement',
          type: 'text',
          rows: 2
        },
        {
          name: 'soilHealth',
          title: 'Soil Health Impact',
          type: 'text',
          rows: 2
        },
        {
          name: 'communityBenefit',
          title: 'Community Benefits',
          type: 'text',
          rows: 3
        }
      ]
    },
    {
      name: 'monitoring',
      title: 'Monitoring & Verification',
      type: 'object',
      fields: [
        {
          name: 'monitoringFrequency',
          title: 'Monitoring Frequency',
          type: 'string',
          options: {
            list: [
              {title: 'Monthly', value: 'monthly'},
              {title: 'Quarterly', value: 'quarterly'},
              {title: 'Semi-annually', value: 'semi_annually'},
              {title: 'Annually', value: 'annually'}
            ]
          }
        },
        {
          name: 'verificationReports',
          title: 'Verification Reports',
          type: 'array',
          of: [{
            type: 'object',
            fields: [
              {
                name: 'reportDate',
                title: 'Report Date',
                type: 'date'
              },
              {
                name: 'verifier',
                title: 'Verifier',
                type: 'string'
              },
              {
                name: 'creditsVerified',
                title: 'Credits Verified',
                type: 'number'
              },
              {
                name: 'reportUrl',
                title: 'Report URL',
                type: 'url'
              }
            ]
          }]
        },
        {
          name: 'satelliteImagery',
          title: 'Satellite Imagery',
          type: 'array',
          of: [{type: 'image'}]
        }
      ]
    },
    {
      name: 'partners',
      title: 'Project Partners',
      type: 'array',
      of: [{
        type: 'object',
        fields: [
          {
            name: 'name',
            title: 'Partner Name',
            type: 'string'
          },
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
      name: 'images',
      title: 'Project Images',
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
          {title: 'Development', value: 'development'},
          {title: 'Certification', value: 'certification'},
          {title: 'Active', value: 'active'},
          {title: 'Trading', value: 'trading'},
          {title: 'Completed', value: 'completed'},
          {title: 'Suspended', value: 'suspended'}
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
      projectType: 'projectType',
      totalCredits: 'carbonMetrics.totalCredits'
    },
    prepare(selection: any) {
      const {title, avatarId, status, projectType, totalCredits} = selection
      return {
        title: title,
        subtitle: `Avatar: ${avatarId} | Type: ${projectType} | Credits: ${totalCredits || 0} | Status: ${status}`
      }
    }
  }
} 