import json

# Load the data from the JSON file
with open('exhibition.json', 'r') as f:
    exhibition = json.load(f)

# Start the new README content
readme_content = f"# {exhibition['name']}\n\n{exhibition['description']}\n\n"

# Add each image to the README content
for image in exhibition['images']:
    readme_content += f"### {image['title']}\n\n![{image['alt']}]({image['url']})\n\n{image['caption']}\n\n"

# Write the new README content to README.md
with open('README.md', 'w') as f:
    f.write(readme_content)
