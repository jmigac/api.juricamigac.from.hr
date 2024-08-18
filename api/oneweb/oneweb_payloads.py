class Payload:

    def __init__(self, response_limit, homepage_id):
        self.EXPERIENCES_PAYLOAD = Payload.get_experiences_payload(response_limit)
        self.PROJECTS_PAYLOAD = Payload.get_projects_payload(response_limit)
        self.HOME_PAGE_PAYLOAD = Payload.get_homepage_payload(response_limit, homepage_id)

    @staticmethod
    def get_homepage_payload(response_limit, homepage_id):
        homepage = """
        {
          homePage(id: "%s") {
            title
            teaser {
              title
              description
              url
              width
              height
            }
            experiencesCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
              items {
                title
                description
                from
                until
              }
            }
            projectsCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
              items {
                title
                description
                technologies
              }
            }
            expertisesCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
              items {
                title
                description
                technologies
              }
            }
            footer {
              socialMediaLinks {
                showLinkedIn
                linkedInUrl
                showGithub
                githubUrl
                showDevTo
                devToUrl 
              }
            }
          }
        }
        """
        return homepage % (homepage_id, response_limit, response_limit, response_limit)

    @staticmethod
    def get_projects_payload(response_limit):
        projects = """
        {
            projectArticleCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
                items {
                    title
                    description
                    technologies
                }
            }
        }
        """
        return projects % response_limit

    @staticmethod
    def get_experiences_payload(response_limit):
        experiences = """
        {
            experienceArticleCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
                items {
                    title
                    description
                    from
                    until
                }
            }
        }
        """
        return experiences % response_limit
