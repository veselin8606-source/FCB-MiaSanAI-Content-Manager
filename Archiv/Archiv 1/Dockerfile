# --- Stufe 1: Build-Phase ---
FROM node:20-slim AS builder

WORKDIR /app

# Abhängigkeiten installieren (inkl. devDependencies)
COPY package*.json ./
RUN npm install

# Quellcode kopieren (hier ist die Korrektur: alles in einer Zeile)
COPY . .
RUN npm run build

# --- Stufe 2: Runtime-Phase (Produktion) ---
FROM node:20-slim

WORKDIR /app

# Nur die Produktions-Abhängigkeiten installieren
COPY package*.json ./
RUN npm install --only=production

# Nur den gebauten dist-Ordner aus dem Builder kopieren
COPY --from=builder /app/dist ./dist

# Port freigeben
EXPOSE 8080

# Start-Kommando
CMD ["npm", "start"]
