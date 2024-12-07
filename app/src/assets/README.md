# `assets` Directory

A place for some static assets for your app.  Images, etc.

TODO: Refactor assets folder into static folder per https://docs.streamlit.io/develop/concepts/configuration/serving-static-files

###
* Directory Description
This folder is designated for storing static assets such as images, icons, CSS files, or other frontend-related static resources. These files are used in the application’s UI to enhance the user experience.

File Description
Currently, this folder contains the following items:

1. logo.png:
The logo image displayed at the top left corner of the application.
When replacing this image, ensure the dimensions and format fit the design. A transparent PNG is recommended.

2. Other Static Resources:
If additional resources (e.g., background images, stylesheets) are needed, place the files in this folder and reference them in your code.

* Usage Instructions
- Referencing Resources: When referencing files in the assets folder, use relative paths. For example, in a Streamlit app, you can reference logo.png as follows:

- Modifying or Replacing Resources:
To replace an existing file (e.g., logo.png), ensure the new file has the same name. Otherwise, you’ll need to update the reference in the code.
When adding new files, make sure to include their paths correctly in the application.

- Optimizing Static Resources:
Compress image files to reduce load time.
Ensure file sizes are reasonable (recommended size <500KB) to improve page performance.