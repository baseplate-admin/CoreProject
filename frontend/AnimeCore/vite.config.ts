import { defineConfig } from "vite";
import { sveltekit } from "@sveltejs/kit/vite";
import path from "path";

export default defineConfig({
    plugins: [sveltekit()],
    legacy: { buildSsrCjsExternalHeuristics: true }, // https://github.com/sveltejs/kit/issues/5549
    resolve: {
        alias: {
            // these are the aliases and paths to them
            $store: path.resolve("./src/lib/store"),
            $hooks: path.resolve("./src/hooks"),
            $components: path.resolve("./src/lib/components"),
            $functions: path.resolve("./src/lib/functions")
        }
    }
});