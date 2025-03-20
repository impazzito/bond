import uuid from "@/utils/uuid";

export default async function* api_call(url, data = {}) {
    console.info("fetch ", url, data);

    const response = await fetch(`//localhost:8500${url}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data), // Send JSON body
    });

    // Handle HTTP errors before processing the stream
    if (!response.ok) {
        try {
            yield yield {
                type: "ValidationError",
                ...(await response.json()),
            };
        } catch (error) {
            console.error("JSON Parse Error:", error);
        }
        return;
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        // Process each complete JSON object (newline-separated)
        let parts = buffer.split("한ЖΩ∑");
        buffer = parts.pop(); // Keep the last incomplete part

        for (let part of parts) {
            if (part.trim()) {
                console.info("received", part);
                try {
                    yield JSON.parse(part);
                } catch (error) {
                    console.error("JSON Parse Error:", error);
                }
            }
        }
    }
}
