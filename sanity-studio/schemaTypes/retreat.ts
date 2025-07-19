export default {
  name: 'retreat',
  title: 'Retreat',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Title',
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
      name: 'avatar',
      title: 'OASIS Avatar',
      type: 'reference',
      to: [{type: 'oasisAvatar'}],
      description: 'The OASIS avatar that created this retreat',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'avatarWallet',
      title: 'Avatar Wallet Address',
      type: 'string',
      description: 'Wallet address for payments and NFT minting'
    },
    {
      name: 'dates',
      title: 'Retreat Dates',
      type: 'object',
      fields: [
        {
          name: 'start',
          title: 'Start Date',
          type: 'date',
          validation: (Rule: any) => Rule.required()
        },
        {
          name: 'end',
          title: 'End Date',
          type: 'date',
          validation: (Rule: any) => Rule.required()
        }
      ]
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
      name: 'price',
      title: 'Price (USD)',
      type: 'number',
      validation: (Rule: any) => Rule.required().min(0)
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
      name: 'maxParticipants',
      title: 'Maximum Participants',
      type: 'number',
      validation: (Rule: any) => Rule.required().min(1)
    },
    {
      name: 'currentParticipants',
      title: 'Current Participants',
      type: 'number',
      initialValue: 0
    },
    {
      name: 'amenities',
      title: 'Amenities',
      type: 'array',
      of: [{type: 'string'}]
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
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          {title: 'Draft', value: 'draft'},
          {title: 'Published', value: 'published'},
          {title: 'Booking Open', value: 'booking_open'},
          {title: 'Fully Booked', value: 'fully_booked'},
          {title: 'Completed', value: 'completed'},
          {title: 'Cancelled', value: 'cancelled'}
        ]
      },
      initialValue: 'draft'
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
      price: 'price'
    },
    prepare(selection: any) {
      const {title, avatarId, status, price} = selection
      return {
        title: title,
        subtitle: `Avatar: ${avatarId} | Status: ${status} | $${price}`
      }
    }
  }
} 