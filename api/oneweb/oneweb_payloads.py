class Payload:

    def __init__(self, response_limit, homepage_id, locale):
        self.EXPERIENCES_PAYLOAD = Payload.get_experiences_payload(response_limit)
        self.PROJECTS_PAYLOAD = Payload.get_projects_payload(response_limit)
        self.HOME_PAGE_PAYLOAD = Payload.get_homepage_payload(response_limit, homepage_id, locale)
        self.FOOTER_PAYLOAD = Payload.get_footer_payload(homepage_id)
        self.EXPERTISES_PAYLOAD = Payload.get_expertises_payload(response_limit)
        self.ABOUT_ME_PAYLOAD = Payload.get_about_me_payload(homepage_id)
        self.TEASER_PAYLOAD = Payload.get_teaser_payload(homepage_id)

    @staticmethod
    def get_homepage_payload(response_limit, homepage_id, locale):
        homepage = """
        {
          homePage(id: "%s", locale: "%s") {
            title
            teaser {
              title
              description
              url
              width
              height
            }
            aboutMe {
                title
                description
            }
            experiencesTitle {
                title
            }
            experiencesCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
              items {
                title
                description
                from
                until
              }
            }
            projectsTitle {
                title
            }
            projectsCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
              items {
                title
                description
                technologies
              }
            }
            expertiseTitle {
                title
            }
            expertisesCollection(limit: %s, order: sys_firstPublishedAt_DESC) {
              items {
                title
                description
                technologies
              }
            }
            footer {
                shareOnSocialMedia {
                  socialMediaLinksCollection {
                    items {
                      icon
                      label
                      linkUrl
                      ariaLabel
                    }
                  }
                }
              socialMediaLinks {
                showLinkedIn
                linkedInUrl
                linkedInAriaLabel
                showGithub
                githubUrl
                githubAriaLabel
                showDevTo
                devToUrl 
                devToAriaLabel
              }
            }
          }
        }
        """
        return homepage % (homepage_id, locale, response_limit, response_limit, response_limit)

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

    @staticmethod
    def get_expertises_payload(response_limit):
        expertises = """
        {
          expertiseCollection(limit: %s) {
            items {
              title
              description
              technologies
            }
          }
        }
        """
        return expertises % response_limit

    @staticmethod
    def get_footer_payload(home_page_id):
        footer = """
        {
            homePage(id: "%s") {
                footer {
                    shareOnSocialMedia {
                      socialMediaLinksCollection {
                        items {
                          icon
                          label
                          linkUrl
                          ariaLabel
                        }
                      }
                    }
                  }
                }  
            }
        """
        return footer % home_page_id

    @staticmethod
    def get_about_me_payload(home_page_id):
        footer = """
        {
            homePage(id: "%s") {
                aboutMe {
                    title
                    description
                }
            }  
        }
        """
        return footer % home_page_id

    @staticmethod
    def get_teaser_payload(home_page_id):
        footer = """
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
            }  
        }
        """
        return footer % home_page_id
