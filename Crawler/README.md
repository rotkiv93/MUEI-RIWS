# Crawler

The crawler is based on scrapy which runs on top of python

Run the crawler with:

```
scrapy crawl myprotein
```

Currently the container installs scrapy dependencies using pip and a requirements.txt file, after that it runs the program which is an spider to get the first titles in myprotein, the output will appear in a data folder, to rerun the code delete the generated file inside.