const error = new Error("429 Too Many Requests");
error.request = { parent: error }; // circular

try {
  const isQuotaError = error?.message?.includes("429") || JSON.stringify(error).includes("429");
  console.log("No crash");
} catch (e) {
  console.log("Crashed:", e.message);
}
