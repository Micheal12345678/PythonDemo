from django import template

t = template.Template('My Name is {{ name }}')
c = template.Context({'name':'Adrian'})
print(t.render(c))