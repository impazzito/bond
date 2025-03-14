
import { randomUUID } from 'node:crypto';

import esbuild from "esbuild"
import vuePlugin from "esbuild-plugin-vue3"
import { sassPlugin } from "esbuild-sass-plugin"

import fs from "fs/promises"
import path from "path"
import { fileURLToPath } from "url"

const build_id = randomUUID();
const __dirname = path.dirname(fileURLToPath(import.meta.url))
const make_path = (...p) => path.resolve(__dirname, ...p)

async function build() {



    const include_paths = [make_path("."), make_path("node_modules")]
    const is_build = process.env.WATCH ? false : true




	const file = 'file';

    // Common options for both modern and legacy builds
	const build_options = async() => ({
        format: "esm",
        sourcemap: true,
        bundle: true,
        splitting: true,
        minify: is_build,
        metafile: is_build,
        entryPoints: ['src/index.js'],
        loader: {
            // file loaders
            ".gif": file,
            ".html": file,
            ".icc": file,
            ".joboptions": file,
            ".jpeg": file,
            ".jpg": file,
            ".mp4": file,
            ".ogg": file,
            ".pdf": file,
            ".png": file,
            ".qfilter": file,
            ".svg": file,
            ".ttf": file,
            ".wasm": file,
            ".webm": file,
            ".woff": file,
            ".woff2": file,
            ".zip": file
        },
        outdir: 'out/',
        plugins: [
            vuePlugin({
                enableTemplateCompiler: true,
            }),
            sassPlugin({
                loadPaths: include_paths,
                type: "css",
                cssModules: false,
                inject: false
            })
        ],
        define: {
            "process.env.NODE_ENV": JSON.stringify(
                is_build ? "production" : "development"
            )
        },
        absWorkingDir: make_path(),
        resolveExtensions: [
            ".js",
            ".vue",
            ".ts"
        ],
        preserveSymlinks: true,
        nodePaths: include_paths,
        // Target specific browser versions based on legacy flag
        target: ["es2020"]
    })

    try {
		if (is_build) {
			// Build version


			console.log(`🔨 Building bundle...`)

			const options = await build_options()

			console.log(
				`⚙️ Configuration:`,
				options
			)

			const bundle = await esbuild.build(options)

		} else {

			// In watch mode, only build modern version
            const ctx = await esbuild.context(await build_options(false))
            await ctx.watch()
            console.log("👀 Watching for changes...")

		}




    } catch (error) {
        console.error("❌ Build failed:", error)
        process.exit(1)
    }
}

build()
