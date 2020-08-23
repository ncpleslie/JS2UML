### parse
Call this to parse any JS file to a UML class diagram. You can exclude the option arguments (filename or directory, the output path and filetype) but the system will ask for you them anyway
Supported output types: 'bmp', 'jpg', 'jpeg', 'pdf', 'png', 'svg', 'webp'
    `parse -f <filename or directory> -o <output> -t <filetype>`
    or
    `parse`

### setup
Setup allows you initialise the program and set the configurations you want. These include default output directory, default output file type, default output name. Setup will even allow you to set a MongoDB as your prefered backup location

### exit
Exits the command line
    `exit`