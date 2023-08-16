#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import openai
openai.api_key = "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"


# In[2]:


app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
            {
                "role": "user",
                "content": q
            }
        ]
    )
        return(render_template("index.html",result=res["choices"][0]["message"]["content"]))
    else:
        return(render_template("index.html",result="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




