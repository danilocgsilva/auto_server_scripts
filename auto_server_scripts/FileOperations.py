class FileOperations:
    
    def generate_file(self, fullFilePath: str, fileContent: str):
        f = open(fullFilePath, "w")
        f.write(fileContent)
        f.close()
        
    def insert_line_in_file(self, file_path, inserting_line_number, line_content):
        f = open(file_path, "r")
        fileContentList = f.readlines()
        f.close()
        fileContentList.insert(inserting_line_number, line_content + "\n")
        modifiedFileString = "".join(fileContentList)
        fileToWrite = open(file_path, "w")
        fileToWrite.write(modifiedFileString)
        fileToWrite.close()