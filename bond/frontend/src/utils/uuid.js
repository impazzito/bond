// UUID7 variant

//export default () => {
//    const value = new Uint8Array(16)
//    crypto.getRandomValues(value)
//    const timestamp = BigInt(Date.now())
//    value[0] = Number((timestamp >> 40n) & 0xffn)
//    value[1] = Number((timestamp >> 32n) & 0xffn)
//    value[2] = Number((timestamp >> 24n) & 0xffn)
//    value[3] = Number((timestamp >> 16n) & 0xffn)
//    value[4] = Number((timestamp >> 8n) & 0xffn)
//    value[5] = Number(timestamp & 0xffn)
//    value[6] = (value[6] & 0x0f) | 0x70
//    value[8] = (value[8] & 0x3f) | 0x80
//    return Array.from(value)
//        .map(b => b.toString(16).padStart(2, "0"))
//        .join("")
//}

export default () =>
    ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
        (
            c ^
            (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
        ).toString(16),
    );
