import os
import re

def search_files(keyword, folder='notes'):
    matches = []
    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.endswith(('.txt', '.md')):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, encoding='utf-8') as f:
                        for line_num, line in enumerate(f, 1):
                            if re.search(keyword, line, re.IGNORECASE):
                                matches.append((filepath, line_num, line.strip()))
                except Exception as e:
                    print(f"❌ Error reading file {filepath}: {e}")
    return matches

if __name__ == '__main__':
    folder = input("📁 Enter folder path (default is 'notes'): ").strip() or 'notes'
    keyword = input("🔍 Enter search keyword: ").strip()

    results = search_files(keyword, folder)

    print("\n" + "=" * 60)
    if results:
        print(f"✅ Found {len(results)} matches for '{keyword}':\n")
        for path, line_no, content in results:
            print(f"📄 File: {path}")
            print(f"   🔢 Line: {line_no}")
            print(f"   📝 Content: *{content}*\n")
        print("=" * 60)
        print("🎉 Search complete!\n")
    else:
        print("⚠️  No matching content found.")
        print("=" * 60)
