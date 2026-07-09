const error = new Error("429 Too Many Requests");
const req = { parent: error };
error.request = req; // enumerable property? No, it's just a property.
try {
  JSON.stringify(error);
  console.log("No crash");
} catch (e) {
  console.log("Crashed:", e.message);
}
