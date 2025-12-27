"""
W3Schools Python & Django Tutorial Downloader
==============================================
این اسکریپت محتوای آموزشی Python و Django را از W3Schools دانلود کرده
و یک فایل HTML آماده پرینت میسازد.

نحوه استفاده:
1. Python 3 را نصب کنید
2. کتابخانه‌های مورد نیاز را نصب کنید:
   pip install requests beautifulsoup4
3. اسکریپت را اجرا کنید:
   python w3schools_to_pdf.py
4. فایل HTML ساخته شده را در مرورگر باز کنید
5. Ctrl+P بزنید و Save as PDF انتخاب کنید
"""

import requests
from bs4 import BeautifulSoup
import time
import os

# ===== تنظیمات =====
SAVE_PYTHON = True      # آموزش Python
SAVE_DJANGO = True      # آموزش Django
OUTPUT_DIR = "."        # پوشه خروجی (همین پوشه)

# ===== لیست صفحات =====

PYTHON_PAGES = [
    # مقدمات
    ("Python Introduction", "python_intro.asp"),
    ("Python Get Started", "python_getstarted.asp"),
    ("Python Syntax", "python_syntax.asp"),
    ("Python Comments", "python_comments.asp"),
    
    # متغیرها
    ("Python Variables", "python_variables.asp"),
    ("Python Variable Names", "python_variables_names.asp"),
    ("Python Assign Multiple Values", "python_variables_multiple.asp"),
    ("Python Output Variables", "python_variables_output.asp"),
    ("Python Global Variables", "python_variables_global.asp"),
    
    # انواع داده
    ("Python Data Types", "python_datatypes.asp"),
    ("Python Numbers", "python_numbers.asp"),
    ("Python Casting", "python_casting.asp"),
    
    # رشته‌ها
    ("Python Strings", "python_strings.asp"),
    ("Python Slicing Strings", "python_strings_slicing.asp"),
    ("Python Modify Strings", "python_strings_modify.asp"),
    ("Python Concatenate Strings", "python_strings_concatenate.asp"),
    ("Python Format Strings", "python_strings_format.asp"),
    ("Python Escape Characters", "python_strings_escape.asp"),
    ("Python String Methods", "python_strings_methods.asp"),
    
    # بولین و عملگرها
    ("Python Booleans", "python_booleans.asp"),
    ("Python Operators", "python_operators.asp"),
    
    # لیست
    ("Python Lists", "python_lists.asp"),
    ("Python Access List Items", "python_lists_access.asp"),
    ("Python Change List Items", "python_lists_change.asp"),
    ("Python Add List Items", "python_lists_add.asp"),
    ("Python Remove List Items", "python_lists_remove.asp"),
    ("Python Loop Lists", "python_lists_loop.asp"),
    ("Python List Comprehension", "python_lists_comprehension.asp"),
    ("Python Sort Lists", "python_lists_sort.asp"),
    ("Python Copy Lists", "python_lists_copy.asp"),
    ("Python Join Lists", "python_lists_join.asp"),
    ("Python List Methods", "python_lists_methods.asp"),
    
    # تاپل
    ("Python Tuples", "python_tuples.asp"),
    ("Python Access Tuples", "python_tuples_access.asp"),
    ("Python Update Tuples", "python_tuples_update.asp"),
    ("Python Unpack Tuples", "python_tuples_unpack.asp"),
    ("Python Loop Tuples", "python_tuples_loop.asp"),
    ("Python Join Tuples", "python_tuples_join.asp"),
    
    # ست
    ("Python Sets", "python_sets.asp"),
    ("Python Access Set Items", "python_sets_access.asp"),
    ("Python Add Set Items", "python_sets_add.asp"),
    ("Python Remove Set Items", "python_sets_remove.asp"),
    ("Python Loop Sets", "python_sets_loop.asp"),
    ("Python Join Sets", "python_sets_join.asp"),
    
    # دیکشنری
    ("Python Dictionaries", "python_dictionaries.asp"),
    ("Python Access Dictionary Items", "python_dictionaries_access.asp"),
    ("Python Change Dictionary Items", "python_dictionaries_change.asp"),
    ("Python Add Dictionary Items", "python_dictionaries_add.asp"),
    ("Python Remove Dictionary Items", "python_dictionaries_remove.asp"),
    ("Python Loop Dictionaries", "python_dictionaries_loop.asp"),
    ("Python Copy Dictionaries", "python_dictionaries_copy.asp"),
    ("Python Nested Dictionaries", "python_dictionaries_nested.asp"),
    
    # شرط‌ها
    ("Python If...Else", "python_conditions.asp"),
    
    # حلقه‌ها
    ("Python While Loops", "python_while_loops.asp"),
    ("Python For Loops", "python_for_loops.asp"),
    
    # توابع
    ("Python Functions", "python_functions.asp"),
    ("Python Lambda", "python_lambda.asp"),
    
    # آرایه‌ها
    ("Python Arrays", "python_arrays.asp"),
    
    # کلاس‌ها
    ("Python Classes/Objects", "python_classes.asp"),
    ("Python Inheritance", "python_inheritance.asp"),
    ("Python Iterators", "python_iterators.asp"),
    ("Python Polymorphism", "python_polymorphism.asp"),
    ("Python Scope", "python_scope.asp"),
    
    # ماژول‌ها
    ("Python Modules", "python_modules.asp"),
    ("Python Dates", "python_datetime.asp"),
    ("Python Math", "python_math.asp"),
    ("Python JSON", "python_json.asp"),
    ("Python RegEx", "python_regex.asp"),
    ("Python PIP", "python_pip.asp"),
    
    # خطاها
    ("Python Try...Except", "python_try_except.asp"),
    ("Python User Input", "python_user_input.asp"),
    ("Python String Formatting", "python_string_formatting.asp"),
    
    # فایل‌ها
    ("Python File Handling", "python_file_handling.asp"),
    ("Python Read Files", "python_file_open.asp"),
    ("Python Write/Create Files", "python_file_write.asp"),
    ("Python Delete Files", "python_file_remove.asp"),
]

DJANGO_PAGES = [
    ("Django Introduction", "django_intro.php"),
    ("Django Get Started", "django_getstarted.php"),
    ("Django Create Virtual Environment", "django_create_virtual_environment.php"),
    ("Django Install", "django_install.php"),
    ("Django Create Project", "django_create_project.php"),
    ("Django Create App", "django_create_app.php"),
    ("Django Views", "django_views.php"),
    ("Django URLs", "django_urls.php"),
    ("Django Templates", "django_templates.php"),
    ("Django Models", "django_models.php"),
    ("Django Insert Data", "django_insert_data.php"),
    ("Django Update Data", "django_update_data.php"),
    ("Django Delete Data", "django_delete_data.php"),
    ("Django Update Model", "django_update_model.php"),
    ("Django QuerySet Introduction", "django_queryset.php"),
    ("Django QuerySet Get", "django_queryset_get.php"),
    ("Django QuerySet Filter", "django_queryset_filter.php"),
    ("Django QuerySet Order By", "django_queryset_orderby.php"),
    ("Django Static Files", "django_static_files.php"),
    ("Django Add Global Static Files", "django_add_global_static.php"),
    ("Django Add Slug Field", "django_slug_field.php"),
    ("Django Add Bootstrap", "django_add_bootstrap.php"),
    ("Django 404 Template", "django_404.php"),
    ("Django Admin", "django_admin.php"),
    ("Django Admin Create User", "django_admin_create_user.php"),
    ("Django Admin Include Model", "django_admin_include_model.php"),
    ("Django Admin Set List Display", "django_admin_set_list_display.php"),
]

# ===== استایل HTML =====
HTML_TEMPLATE = """<!DOCTYPE html>
<html dir="ltr" lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        * {{
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 850px;
            margin: 0 auto;
            padding: 30px;
            line-height: 1.7;
            color: #333;
            background: #fff;
        }}
        
        /* Cover Page */
        .cover {{
            text-align: center;
            padding: 100px 20px;
            page-break-after: always;
        }}
        .cover h1 {{
            font-size: 3em;
            color: #04AA6D;
            margin-bottom: 20px;
            border: none;
        }}
        .cover p {{
            font-size: 1.3em;
            color: #666;
        }}
        
        /* Headings */
        h1 {{
            color: #04AA6D;
            font-size: 1.8em;
            border-bottom: 3px solid #04AA6D;
            padding-bottom: 10px;
            margin-top: 40px;
            page-break-before: always;
        }}
        h1:first-of-type {{
            page-break-before: avoid;
        }}
        h2 {{
            color: #333;
            font-size: 1.4em;
            margin-top: 30px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 5px;
        }}
        h3 {{
            color: #555;
            font-size: 1.1em;
            margin-top: 20px;
        }}
        
        /* Paragraphs */
        p {{
            margin: 12px 0;
            text-align: justify;
        }}
        
        /* Code */
        pre, .code-block {{
            background: #f8f8f8;
            border: 1px solid #e0e0e0;
            border-left: 4px solid #04AA6D;
            border-radius: 4px;
            padding: 15px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
            overflow-x: auto;
            margin: 15px 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        code {{
            background: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        
        /* Example Box */
        .example {{
            background: #f9fff9;
            border: 1px solid #04AA6D;
            border-radius: 5px;
            padding: 15px;
            margin: 20px 0;
        }}
        .example-title {{
            font-weight: bold;
            color: #04AA6D;
            margin-bottom: 10px;
        }}
        
        /* Result Box */
        .result {{
            background: #fff;
            border: 2px solid #04AA6D;
            border-radius: 5px;
            padding: 10px 15px;
            margin: 10px 0;
        }}
        .result-title {{
            font-size: 0.85em;
            color: #04AA6D;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        /* Note Box */
        .note {{
            background: #fffde7;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 15px 0;
        }}
        
        /* Tables */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            font-size: 0.95em;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 10px 12px;
            text-align: left;
        }}
        th {{
            background: #04AA6D;
            color: white;
            font-weight: 600;
        }}
        tr:nth-child(even) {{
            background: #f9f9f9;
        }}
        tr:hover {{
            background: #f1f1f1;
        }}
        
        /* Lists */
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        
        /* Print Styles */
        @media print {{
            body {{
                padding: 20px;
                font-size: 11pt;
            }}
            h1 {{
                page-break-before: always;
                font-size: 16pt;
            }}
            h1:first-of-type {{
                page-break-before: avoid;
            }}
            pre {{
                white-space: pre-wrap;
                word-wrap: break-word;
                font-size: 9pt;
            }}
            .cover {{
                page-break-after: always;
            }}
        }}
    </style>
</head>
<body>
<div class="cover">
    <h1>{title}</h1>
    <p>Based on W3Schools Tutorial</p>
    <p style="color: #999; margin-top: 50px;">Ready for Print & Highlight</p>
</div>
{content}
</body>
</html>
"""

# ===== توابع =====

def get_page(url):
    """دریافت محتوای صفحه"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None

def extract_content(html, title):
    """استخراج محتوای اصلی از صفحه"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # پیدا کردن بخش اصلی
    main = soup.find('div', {'id': 'main'})
    if not main:
        main = soup.find('div', class_='w3-col')
    if not main:
        return f"<h1>{title}</h1><p>Content not found</p>"
    
    content_parts = [f"<h1>{title}</h1>"]
    
    # استخراج المان‌ها
    for elem in main.find_all(['h1', 'h2', 'h3', 'p', 'pre', 'div', 'table', 'ul', 'ol']):
        # رد کردن المان‌های ناخواسته
        classes = elem.get('class', [])
        if isinstance(classes, list):
            classes_str = ' '.join(classes)
        else:
            classes_str = str(classes)
        
        skip_classes = ['w3-btn', 'w3-bar', 'w3-right', 'w3-left', 'w3-hide', 'w3-button']
        if any(skip in classes_str for skip in skip_classes):
            continue
        
        # h2, h3
        if elem.name == 'h2':
            text = elem.get_text(strip=True)
            if text and len(text) > 1:
                content_parts.append(f"<h2>{text}</h2>")
        
        elif elem.name == 'h3':
            text = elem.get_text(strip=True)
            if text and len(text) > 1:
                content_parts.append(f"<h3>{text}</h3>")
        
        # پاراگراف
        elif elem.name == 'p':
            text = elem.get_text(strip=True)
            if text and len(text) > 3:
                # تبدیل کدهای inline
                html_content = str(elem)
                html_content = html_content.replace('<code>', '<code>').replace('</code>', '</code>')
                content_parts.append(f"<p>{text}</p>")
        
        # کد
        elif elem.name == 'pre' or (elem.name == 'div' and 'w3-code' in classes_str):
            code = elem.get_text()
            if code and code.strip():
                content_parts.append(f'<pre>{code.strip()}</pre>')
        
        # مثال
        elif elem.name == 'div' and 'w3-example' in classes_str:
            example_title = elem.find(['h3', 'h4'])
            example_code = elem.find('pre') or elem.find('div', class_='w3-code')
            
            parts = ['<div class="example">']
            if example_title:
                parts.append(f'<div class="example-title">{example_title.get_text(strip=True)}</div>')
            if example_code:
                parts.append(f'<pre>{example_code.get_text().strip()}</pre>')
            parts.append('</div>')
            content_parts.append('\n'.join(parts))
        
        # جدول
        elif elem.name == 'table':
            content_parts.append(str(elem))
        
        # لیست
        elif elem.name in ['ul', 'ol']:
            content_parts.append(str(elem))
    
    return '\n'.join(content_parts)

def create_tutorial(pages, base_url, title, filename):
    """ساخت فایل HTML از صفحات"""
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}")
    
    all_content = []
    success = 0
    
    for page_title, page_url in pages:
        full_url = base_url + page_url
        print(f"  [{success+1}/{len(pages)}] {page_title}...", end=" ", flush=True)
        
        html = get_page(full_url)
        if html:
            content = extract_content(html, page_title)
            all_content.append(content)
            print("✓")
            success += 1
        else:
            print("✗")
        
        time.sleep(0.3)  # احترام به سرور
    
    # ساخت فایل نهایی
    final_html = HTML_TEMPLATE.format(
        title=title,
        content='\n'.join(all_content)
    )
    
    output_path = os.path.join(OUTPUT_DIR, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"\n  ✓ Saved: {output_path}")
    print(f"  ✓ Pages: {success}/{len(pages)}")
    
    return output_path

# ===== اجرا =====

if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════════╗
║     W3Schools Tutorial Downloader                     ║
║     Python & Django → HTML (Ready for PDF)            ║
╚═══════════════════════════════════════════════════════╝
    """)
    
    created_files = []
    
    if SAVE_PYTHON:
        path = create_tutorial(
            PYTHON_PAGES,
            "https://www.w3schools.com/python/",
            "Python Tutorial - W3Schools",
            "Python_Tutorial_W3Schools.html"
        )
        created_files.append(path)
    
    if SAVE_DJANGO:
        path = create_tutorial(
            DJANGO_PAGES,
            "https://www.w3schools.com/django/",
            "Django Tutorial - W3Schools",
            "Django_Tutorial_W3Schools.html"
        )
        created_files.append(path)
    
    print(f"""
{'='*50}
  ✅ DONE!
{'='*50}

Created files:
""")
    for f in created_files:
        print(f"  • {f}")
    
    print("""
Next steps:
  1. Open the HTML file in your browser
  2. Press Ctrl+P (or Cmd+P on Mac)
  3. Select "Save as PDF"
  4. Print and highlight!

Enjoy learning! 🐍
""")