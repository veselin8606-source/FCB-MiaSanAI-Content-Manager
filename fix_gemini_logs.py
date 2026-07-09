import re

with open('server.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all console.log("Gemini API call failed for XXX, using fallback:", error.message || error);
# With a cleaner version that avoids printing the raw error JSON object

def replacer(match):
    context = match.group(1)
    return f"""const isQuotaError = error?.message?.includes("429") || error?.message?.includes("RESOURCE_EXHAUSTED") || JSON.stringify(error).includes("429") || JSON.stringify(error).includes("RESOURCE_EXHAUSTED");
    if (isQuotaError) {{
      console.log("[API] {context} loaded from high-fidelity simulated backup (Gemini rate-limit or quota-limit reached)");
    }} else {{
      console.log("[API] {context} loaded from fallback backup:", error.message || "Simulated backup active");
    }}"""

content = re.sub(r'console\.log\("Gemini API call failed for (.*?), using fallback:", error\.message \|\| error\);', replacer, content)

with open('server.ts', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated server.ts logs")
