#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image


# In[6]:


image = Image.open('C:\\python\\sample_image\\table01.jpg')
r,g,b = image.split()
convert_image = Image.merge("RGB",(b,g,r))
convert_image.show()
convert_image.save('C:\\python\\sample_image\\rgb_to_bgr.jpg');


# In[8]:


black_and_while = image.convert('1')
black_and_while.show()
black_and_while .save('C:\\python\\sample_image\\b_and_w.jpg')


# In[9]:


black_and_while = image.convert('L')
black_and_while.show()
black_and_while .save('C:\\python\\sample_image\\gary_image.jpg')


# In[11]:


image.transpose(Image.ROTATE_90).show()
image.transpose(Image.ROTATE_90).save('C:\\python\\sample_image\\grotate_90.jpg')


# In[ ]:




