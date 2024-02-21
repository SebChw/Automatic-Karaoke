<p><a target="_blank" href="https://app.eraser.io/workspace/vB5CVeoWtzeL9Fv6T5E0" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

### Automatic-Karaoke
## Functional requirements 
- User can upload mp4 or mp3 file and obtain version without specified instrument
- User can specify 4 instruments to be removed:
    - drums
    - bass
    - guitar
    - vocal
- User can select whether output is mp3 or mp4 file
- When user selects mp4 additional options are shown:
    - To extract text
    - To upload a custom image
    - To generate image using SD
- If user selects vocals additionally 2 options are available
    - To add a melody to help singing (just in case of vocals)
    - To add circle jumping around the text
## Non Functional requirements
- Every request is saved to storage so that if someone requests a song that was already processed then we don't run processing again:
    - Preferably separated vocals, drums etc. are put into some blob storage
    - metadata such as text, title, number of downloads etc are put in some database
![Azure Setup](/.eraser/vB5CVeoWtzeL9Fv6T5E0___1OicjVxUrAdzZsO7W8e4NIGYbvx2___---figure---vb85ApMnFh0f2ZPL6jm2g---figure---RlcAaVM1DwZGb1FvKj4d5g.png "Azure Setup")




<!--- Eraser file: https://app.eraser.io/workspace/vB5CVeoWtzeL9Fv6T5E0 --->