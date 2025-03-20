import asyncio


async def join_generators(*generators):
    # No generators provided
    if not generators:
        return

    # Create initial tasks for all generators
    pending = {}
    for gen in generators:
        pending[asyncio.create_task(anext(gen, None))] = gen

    # Continue until all generators are exhausted
    while pending:
        # Wait for the first result to be ready
        done, _ = await asyncio.wait(pending.keys(), return_when=asyncio.FIRST_COMPLETED)

        # Process completed tasks
        for task in done:
            generator = pending.pop(task)
            try:
                result = task.result()

                # If not at the end of the generator, yield the result
                # and create a new task for the next value
                if result is not None:
                    yield result
                    pending[asyncio.create_task(anext(generator, None))] = generator
            except StopAsyncIteration:
                # Generator is exhausted, nothing to do
                pass
