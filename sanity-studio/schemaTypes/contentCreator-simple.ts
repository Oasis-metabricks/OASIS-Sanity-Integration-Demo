export default {
  name: 'contentCreatorSimple',
  title: 'Content Creator (Simple)',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Content Title',
      type: 'string'
    },
    {
      name: 'contentType',
      title: 'Content Type',
      type: 'string',
      options: {
        list: [
          {title: 'Blog Post', value: 'blog_post'},
          {title: 'Article', value: 'article'},
          {title: 'Tutorial', value: 'tutorial'}
        ]
      }
    },
    {
      name: 'avatarId',
      title: 'OASIS Avatar ID',
      type: 'string'
    },
    {
      name: 'description',
      title: 'Description',
      type: 'text'
    },
    {
      name: 'body',
      title: 'Body',
      type: 'array',
      of: [
        {
          type: 'block'
        },
        {
          type: 'image',
          options: {
            hotspot: true
          }
        }
      ]
    },
    {
      name: 'category',
      title: 'Category',
      type: 'string',
      options: {
        list: [
          {title: 'Technology', value: 'technology'},
          {title: 'Web3', value: 'web3'},
          {title: 'Blockchain', value: 'blockchain'}
        ]
      }
    },
    {
      name: 'status',
      title: 'Status',
      type: 'string',
      options: {
        list: [
          {title: 'Draft', value: 'draft'},
          {title: 'Published', value: 'published'}
        ]
      }
    }
  ]
} 