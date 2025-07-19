export default {
  name: 'retreatSimple',
  title: 'Retreat (Simple)',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Title',
      type: 'string'
    },
    {
      name: 'description',
      title: 'Description',
      type: 'text'
    },
    {
      name: 'avatarId',
      title: 'OASIS Avatar ID',
      type: 'string'
    },
    {
      name: 'price',
      title: 'Price (USD)',
      type: 'number'
    },
    {
      name: 'location',
      title: 'Location',
      type: 'string'
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          {title: 'Draft', value: 'draft'},
          {title: 'Published', value: 'published'},
          {title: 'Booking Open', value: 'booking_open'}
        ]
      }
    }
  ]
} 