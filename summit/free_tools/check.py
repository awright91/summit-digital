import requests
from bs4 import BeautifulSoup

class Check():
    def __init__(self, url, keyword, location, page_errors, page_passing, errors_count=0, passing_count=0, kw_density=0, loc_density=0):
        self.url = url
        self.keyword = keyword.lower()
        self.location = location.lower()
        self.page_errors = page_errors
        self.page_passing = page_passing
        self.errors_count = errors_count
        self.passing_count = passing_count
        self.kw_density = kw_density
        self.loc_density = loc_density

    def make_initial_request(self):
        try:
            soup_request = requests.get(self.url)
            content = soup_request.content
            soup = BeautifulSoup(content, 'html.parser')
            return soup
        except requests.exceptions.ConnectionError:
            requests.status_code = "Could Not Find URL"
            return ''



    def check_title(self, soup):
        title_element = str(soup.find('title').get_text(" ", strip = True)).lower()
        title_len = int(len(title_element))

        if title_element is None:
            self.page_errors.append('You Have No Page Title.')
            self.errors_count += 1
        else:
            self.page_passing.append('You Have a Page Title.')
            self.passing_count += 1
            if title_len > 70:
                self.page_errors.append('Page Title is too long. We Recommend a page title no longer than 70 Characters')
                self.errors_count += 1
            else:
                self.passing_count += 1
                self.page_passing.append('Your page title is an appropriate length.')

            if self.keyword in title_element:
                self.passing_count += 1
                self.page_passing.append('Your keyword is in your page title.')
            else:
                self.errors_count += 1
                self.page_passing.append("Your keyword is not in your title")

            if self.location in title_element:
                self.passing_count += 1
                self.page_passing.append('Your location is in your page title.')
            else:
                self.page_errors.append('Your Location is not in your title')
                self.errors_count += 1

    def check_meta(self, soup):
        description = soup.find('meta', attrs={'name':'og:description'}) or soup.find('meta', attrs={'property':'description'}) or soup.find('meta', attrs={'name':'description'})

        if description:
            self.passing_count += 1
            self.page_passing.append('You have a Meta Description')
        else:
            self.page_errors.append("There is no Meta Description on your page.")
            self.errors_count += 1


    def check_h1(self, soup):
        h1_elements = soup.find_all('h1')

        h1_element = str(soup.find('h1')).lower()

        if len(h1_elements) > 1:
            self.page_errors.append('You have too many H1s, we suggest having only 1.')
            self.errors_count += 1
        else:
            self.passing_count += 1
            self.page_passing.append('You have only 1 H1 on this page.')

        if self.keyword in h1_element:
            self.passing_count += 1
            self.page_passing.append('Your keyword is in your H1.')
        else:
            self.errors_count += 1
            self.page_errors.append("Your keyword is not in your H1")


    def check_headers(self, soup):
        h2_elements = soup.find_all('h2')
        h3_elements = soup.find_all('h3')

        if h2_elements is None:
            self.errors_count += 1
            self.page_errors.append("You Don't have an H2 on this page.")
        else:
            self.passing_count += 1
            self.page_passing.append("You have an H2 on your page.")
        if h3_elements is None:
            self.errors_count += 1
            self.page_errors.append("You Don't have an H3 on this page.")
        else:
            self.passing_count += 1
            self.page_passing.append("You have an H3 on your page.")


    def check_imgs(self, soup):
        img_elements = soup.find_all('img')

        for img in img_elements:
            if img.has_attr('alt'):
                self.passing_count += 1
                self.page_passing.append('One of your images has an ALT attribute.')
            else:
                if img.has_attr('src'):
                    bad_img = img['src']
                    self.errors_count += 1
                    self.page_errors.append("The Image: {} doesn't have an Alt Attribute".format(bad_img))
                else:
                    self.errors_count += 1
                    self.page_errors.append("One image is broken, or doesn't have a SRC attribute.")

    def content_checks(self, soup):
        body_element = soup.find('body').get_text(" ", strip = True).lower()
        body_len = int(len(body_element.split()))
        keyword_count = body_element.count(self.keyword)
        kw_density_ratio = (keyword_count / body_len) * 100
        location_count = body_element.count(self.location)
        location_density_ratio = (location_count / body_len) * 100

        self.kw_density = round(kw_density_ratio, 2)
        self.loc_density = round(location_density_ratio, 2)

        if body_len < 400:
            self.errors_count += 1
            self.page_errors.append("Your Content has {} words, and is too short. We suggest at least 500 words per page.".format(body_len))
        else:
            self.passing_count += 1
            self.page_passing.append("Your page's text content is an appropriate length.")

        if kw_density_ratio < 2.0:
            self.errors_count += 1
            self.page_errors.append("Your Keyword Desnity is {}, we recommend a 2% Keyword Density".format(kw_density_ratio))
        else:
            self.passing_count += 1
            self.page_passing.append('Your keyword density is above 2%')

        if location_density_ratio < 1.5:
            self.errors_count += 1
            self.page_errors.append("Your Location Keyword Desnity is {}, we recommend a 1.5% Location Keyword Density".format(location_density_ratio))
        else:
            self.passing_count += 1
            self.page_passing.append('Your location keyword density is above 1.5%')
