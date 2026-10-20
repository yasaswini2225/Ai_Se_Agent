// DevPulse AI - Node.js Async Simulation
const simulateTask = (name, delay) => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(`[${new Date().toISOString().slice(11, 19)}] Task '${name}' completed in ${delay}ms`);
    }, delay);
  });
};

async function runPipeline() {
  console.log("⚡ Initiating Async Microservices Pipeline...");
  const tasks = [
    simulateTask("Auth-Service", 200),
    simulateTask("Database-Fetch", 450),
    simulateTask("Cache-Warmup", 150),
    simulateTask("Analytics-Stream", 300)
  ];

  const results = await Promise.all(tasks);
  results.forEach(res => console.log(res));
  console.log("🎉 All 4 pipeline stages executed synchronously in parallel!");
}

runPipeline();
