import re

with open('server.ts', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    context = match.group(1)
    return f"""const isQuotaError = err?.message?.includes("429") || err?.message?.includes("RESOURCE_EXHAUSTED") || JSON.stringify(err).includes("429") || JSON.stringify(err).includes("RESOURCE_EXHAUSTED");
        if (isQuotaError) {{
          console.log("[IMAGE GEN] {context} request loaded from simulated backup (rate-limit)");
        }} else {{
          console.log("[IMAGE GEN] {context} request failed:", err.message || err);
        }}"""

content = re.sub(r'console\.log\("\[IMAGE GEN\] (.*?) request failed:", err\.message \|\| err\);', replacer, content)

with open('server.ts', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated server.ts image fallback logs")
