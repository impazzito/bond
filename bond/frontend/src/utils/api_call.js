export default async function* api_call(url) {

    console.log('fetch ', url)


    const response = await fetch(`//localhost:8500${url}`);
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";


    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        // Process each complete JSON object (newline-separated)
        let parts = buffer.split("\n");
        buffer = parts.pop();  // Keep the last incomplete part

        for (let part of parts) {
            if (part.trim()) {
                try {
                    yield JSON.parse(part);  // Yield each parsed JSON object
                } catch (error) {
                    console.error("JSON Parse Error:", error);
                }
            }
        }
    }
}