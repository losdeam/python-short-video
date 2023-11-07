import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import ElementPlus from 'unplugin-element-plus/vite'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
    plugins: [
        vue(),
        ElementPlus({
            importStyle: 'css',
            useSource: true
        }),
        AutoImport({
            resolvers: [ElementPlusResolver()],
        }),
        Components({
            resolvers: [ElementPlusResolver()],
        }),
    ],

    server: {
        port: 18080,
        host: '0.0.0.0',
        // https: true,
    },
    resolve: {
        alias: [
            {
                find: '@/',
                replacement: '/src/'
            }
        ],
    }
})
