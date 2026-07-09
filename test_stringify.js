import { GoogleGenAI } from "@google/genai";

async function run() {
  const ai = new GoogleGenAI({ apiKey: "FAKE_KEY_THAT_FAILS" });
  try {
    await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: "Hello"
    });
  } catch (error) {
    try {
      JSON.stringify(error);
      console.log("Stringify succeeded");
    } catch (e) {
      console.error("Stringify failed:", e.message);
    }
  }
}
run();
