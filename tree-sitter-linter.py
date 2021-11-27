import sys
import csv
from argparse import ArgumentParser
from tree_sitter import Language, Parser
from githubfile_fetch import get_file_contents
from identifierChecker import namingConventionCheck

def main():
  parser = ArgumentParser()
  parser.add_argument("-i", "--gitHub", dest="gitHub",
                        help="specify the github url", metavar="GITHUB-URL")
  parser.add_argument("-e", "--extension", dest="extension",
                        help="specify the extension of file", metavar="extension")
  parser.add_argument("-l", "--language", dest="language",
                        help="specify the language of file", metavar="language")
  parser.add_argument("-m", "--filepath1", dest="filepath1",
                        help="specify the filepath along with the filename for output1", metavar="filepath1")
  parser.add_argument("-n", "--filepath2", dest="filepath2",
                        help="specify the filepath along with the filename for output2", metavar="filepath2")
  args = parser.parse_args()
  accepted_languages = ['python', 'javascript', 'ruby', 'go']
  accepted_extensions = ['.py', '.js', '.rb', '.go']
  
  if args.gitHub is None:
        print("Please specify the github url")
        print("use the -h option to see usage information")
        sys.exit(2)
  elif args.extension is None or args.extension not in accepted_extensions:
        print("Please specify the extension: eg: .py, .js, .rb, .go")
        print("use the -h option to see usage information")
        sys.exit(2)
  elif args.language is None or args.language not in accepted_languages:
        print("Please specify the language: eg:python, javascript,ruby, go")
        print("use the -h option to see usage information")
        sys.exit(2)
  elif args.filepath1 is None:
        print("Please specify the path to the output1 along with filename eg:output/output1.csv")
        print("use the -h option to see usage information")
        sys.exit(2)
  elif args.filepath2 is None:
        print("Please specify the path to the output2 along with filename eg:output/output2.csv")
        print("use the -h option to see usage information")
        sys.exit(2)
  else:
        gitHubURL = args.gitHub
        extension = args.extension
        language = args.language
        filepath1 = args.filepath1
        filepath2 = args.filepath2
  
  Language.build_library(
    # Store the library in the `build` directory
    'build/my-languages.so',

    # Include one or more languages
    [
      'languages/tree-sitter-go',
      'languages/tree-sitter-ruby',
      'languages/tree-sitter-javascript',
      'languages/tree-sitter-python'
    ]
  )

  SEL_LANGUAGE = Language('build/my-languages.so', language)

  parser = Parser()
  parser.set_language(SEL_LANGUAGE)

  file_content_list = get_file_contents(gitHubURL,extension)
  identifier_list = []
  identifier_details = {}

  for i in range(len(file_content_list)):
      
    source = file_content_list[i].decoded_content
    file_path = file_content_list[i].path

    tree = parser.parse(source)

    query = SEL_LANGUAGE.query(
          """((identifier) @x)
          """
    )

    captures = query.captures(tree.root_node)
    strList = source.split(b'\n')
    
    for i in range(len(captures)):
      line_number = captures[i][0].start_point[0]
      start_index = captures[i][0].start_point[1]
      end_index =  captures[i][0].end_point[1]

      name_identifier = strList[line_number][start_index:end_index].decode('utf-8')
      failed_list = []
      # print(name_identifier)
      failed_list = namingConventionCheck(name_identifier)
      # print(failed_list)
      identifier_details = {
        "filepath" : file_path,
        "line_number" : line_number,
        "start_index" : start_index,
        "end_index" : end_index,
        "name" : name_identifier,
        "rules_violated" : failed_list
      }
      identifier_list.append(identifier_details)
      

  # names_list = []
  # for i in range(len(identifier_list)):
  #       names_list.append(identifier_list[i]['name'])
  # # print(names_list)
  # failed_list = []
  # failed_list = namingConventionCheck(names_list)
  # print(failed_list)
  # print(identifier_list)
  
  fields = ['filepath', 'line_number', 'start_index', 'end_index','name']
  with open(filepath1, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for item in identifier_list:
      writer.writerow([item['filepath'], item['line_number'], item['start_index'],item['end_index'], item['name']])
      
  output2_fields = ['filepath', 'line_number', 'start_index', 'end_index','name','rules_violated']
  s=':'
  with open(filepath2, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(output2_fields)
    for item in identifier_list:
      writer.writerow([item['filepath'], item['line_number'], item['start_index'],item['end_index'], item['name'], s.join(item['rules_violated'])])
                
if __name__ == "__main__":
    main()
  