# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser
meta = 0
class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print ("comment encountered")
    current_pos = self.getpos()
    print ("At the position " + str(current_pos[0]))

  def handle_data(self, data):
    if (data.isspace()):
      return
    print ("data encountered")
    current_pos = data.getpos()
    print ("At the position" + str(current_pos[0]))
  
  def handle_starttag (self, tag, attr):
    print ('encountered a start tag' + tag)
    if 
    pass

  def handle_endtag (self, tag):
    print ('tag encountered' +  tag)
    current_pos = tag.getpos()
    print ('At the position' + str(current_pos[0]))

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("samplehtml.html")
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)   

if __name__ == "__main__":
  main()
  