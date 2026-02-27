import os
import re
import math

def fix_home_html():
    with open('d:/project/mironix/home.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace category buttons
    content = content.replace('data-filter="sr">Sr</button>', 'data-filter="storage-racks">Storage Racks</button>')
    content = content.replace('data-filter="ws">Ws</button>', 'data-filter="wall-seperator">Wall Seperator</button>')

    # Replace icons mapping
    content = content.replace("'sr': 'package',", "'storage-racks': 'package',")
    content = content.replace("'ws': 'layout',", "'wall-seperator': 'layout',")

    # Replace products
    # We'll use a regex to carefully replace 'sr' and 'ws' in the products list
    content = re.sub(r"category:\s*'sr',\s*title:\s*'Sr\s+(\d+)'", r"category: 'storage-racks', title: 'Storage Racks \1'", content)
    content = re.sub(r"desc:\s*'Premium sr\s+(\d+)\s+for your space.'", r"desc: 'Premium storage racks \1 for your space.'", content)

    content = re.sub(r"category:\s*'ws',\s*title:\s*'Ws\s+(\d+)'", r"category: 'wall-seperator', title: 'Wall Seperator \1'", content)
    content = re.sub(r"desc:\s*'Premium ws\s+(\d+)\s+for your space.'", r"desc: 'Premium wall seperator \1 for your space.'", content)

    with open('d:/project/mironix/home.html', 'w', encoding='utf-8') as f:
        f.write(content)


def generate_school_data():
    base_dir = r"d:\project\mironix\images\institutional"
    
    categories = []
    if os.path.exists(base_dir):
        categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
        
    prices = {
        'benches': 14000,
        'labs': 35000,
        'library': 22000
    }
    
    products_js = "        const products = [\n"
    idx = 1
    for category in categories:
        cat_path = os.path.join(base_dir, category)
        files = []
        for file in os.listdir(cat_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                files.append(file)
        
        # Sort files simply by name for consistent output
        files.sort()
        start_price = prices.get(category, 10000)
        
        for file in files:
            title = f"{category.capitalize()} {idx}"
            if category == 'labs':
                title = f"Lab Equipment {idx}"
            price = start_price + (idx * 500)
            img_path = f"images/institutional/{category}/{file}"
            desc = f"Premium {category} {idx} for institutional spaces."
            products_js += f"            {{ id: {idx}, category: '{category}', title: '{title}', price: '₹ {price}', img: '{img_path}', desc: '{desc}' }},\n"
            idx += 1
    
    products_js += "        ];\n"
    
    # Generate the filter buttons block
    buttons_html = """                <div id="filter-bar"
                    class="flex flex-nowrap items-center gap-4 md:gap-8 min-w-max pb-4 px-2 md:justify-center">
                    <button
                        class="category-btn active text-[10px] font-bold tracking-[0.2em] uppercase py-2 px-6 rounded-full border border-[#2c1e14] bg-[#2c1e14] text-white transition-all duration-300"
                        data-filter="all">All</button>\n"""
    
    for category in categories:
        buttons_html += f"""                    <button
                        class="category-btn text-[10px] font-bold tracking-[0.2em] uppercase py-2 px-6 rounded-full border border-[#2c1e14]/20 hover:border-[#2c1e14] transition-all duration-300"
                        data-filter="{category}">{category.capitalize()}</button>\n"""
                        
    buttons_html += "                </div>"
    
    # Generate the getIcon function
    geticon_js = """        function getIcon(category) {
            const icons = {
                'benches': 'student',
                'labs': 'flask',
                'library': 'books'
            };
            return icons[category] || 'graduation-cap';
        }"""
        
    # Read school.html
    with open('d:/project/mironix/school.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace buttons
    content = re.sub(
        r'<div id="filter-bar".*?</div>', 
        buttons_html, 
        content, 
        flags=re.DOTALL
    )
    
    # Replace navigation so 'Institutional' matches others (text-brown color instead of active bg?) Actually wait, navigation active class in school.html is just simple text color.
    # Replace products array
    content = re.sub(
        r'\bconst products = \[\s*\{.*?\}\s*\];', 
        products_js.strip(), 
        content, 
        flags=re.DOTALL
    )

    # Replace getIcon
    content = re.sub(
        r'function getIcon\(category\) \{.+?return icons\[category\] \|\| \'.+?\';\s*\}', 
        geticon_js, 
        content, 
        flags=re.DOTALL
    )
    
    with open('d:/project/mironix/school.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done generating school.html and updating home.html")

if __name__ == "__main__":
    fix_home_html()
    generate_school_data()
