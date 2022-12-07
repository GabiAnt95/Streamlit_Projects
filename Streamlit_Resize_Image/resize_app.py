import streamlit as st
from os import remove

from PIL import Image

def resize_image(file, x, y):
    return Image.open(file).resize((x, y))

st.title('Resize Images for Free:')

st.header("""

-------------------- 5 STEPS -----------------------

1) Upload your image
2) Introduce the new Pixel size
3) See the result
4) If you do not like it: Come back to 2)
5) If you like it: Click on Download:)

""")

image = st.file_uploader('Upload a .png or .jpg', type=['.png', 'jpg'])

x = int(st.number_input('Horizontal pixels'))
y = int(st.number_input('Vertical pixels'))
print(image)
if image != None and x > 0 and y > 0:
    result = resize_image(image, x, y)
    result.save('Resized_' + str(x) + 'x' + str(y) + '.png')
    st.image(result)
    with open('Resized_' + str(x) + 'x' + str(y) + '.png', "rb") as file:
        st.download_button("Download Image: ", file, file_name = 'Resized_' + str(x) + 'x' + str(y) + '.png', mime="image/png")
        file.close()
        remove('Resized_' + str(x) + 'x' + str(y) + '.png')
elif image == None:
    st.subheader('No image has been uploaded yet:(')
else:
    st.subheader('Give some values to resize!')
