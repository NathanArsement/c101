import dropbox
import os
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload_File(self,file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(file_from):
            print("UPLOADED!")
            for fileName in files:
                
                localPath=os.path.join(root,fileName)
                relPath=os.path.relpath(localPath, file_from)
                dropboxpath=os.path.join(file_to, relPath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))
                    
def main():
    access_token='--O5qpIInasAAAAAAAAAAVQkBUIUA5uAP7s91hF-Lz7fG-Pw3Rxrh5RJ4pyo5vzP'
    transferData=TransferData(access_token)
    file_from='test.txt'
    file_to='/whjr/test.txt'
    transferData.upload_File(file_from, file_to)
    

main()
