# returns domain name of url 
def get_domain_name(url):
  
  # error message if input isn't string
  if type(url) != str:
    print('Error: Input must be a string')
    return
  
  // split url on '/' or '.'
  split_url = url.split('/') if '/' in url else url.split('.')
  if len(split_url) > 2: 
    # get second element of split URL(domain name)
    domain_name = split_url[2]
    # split domain name on '.' 
    split_domain_name = domain_name.split('.')
  else: 
    domain_name=''
    return
  
  # return first element of split domain name (domain name without the top level domain)
  return split_domain_name[0]

#tests 
print(get_domain_name("http://github.com")) # "github"
print(get_domain_name("http://www.google.com")) # "google"
print(get_domain_name("https://www.cnet.com")) # "cnet"
