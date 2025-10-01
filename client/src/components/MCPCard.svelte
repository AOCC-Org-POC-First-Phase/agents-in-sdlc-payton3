<script lang="ts">
    export let title: string;
    export let description: string;
    export let type: string; // "Local" or "Remote"
    export let vendor: string;
    export let vendorLogo: string = "";
</script>

<div class="group block bg-slate-800/60 backdrop-blur-sm rounded-xl overflow-hidden shadow-lg border border-slate-700/50 hover:border-blue-500/50 hover:shadow-blue-500/10 hover:shadow-xl transition-all duration-300 hover:translate-y-[-4px]">
    <div class="p-6 relative">
        <div class="absolute inset-0 bg-gradient-to-r from-blue-600/10 to-purple-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        <div class="relative z-10">
            <div class="flex gap-2 mb-3">
                <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-blue-900/60 text-blue-300">
                    MCP
                </span>
                <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-purple-900/60 text-purple-300">
                    {type}
                </span>
            </div>
            
            <h3 class="text-xl font-semibold text-slate-100 mb-2 group-hover:text-blue-400 transition-colors">
                {title}
            </h3>
            
            <p class="text-slate-400 mb-4 text-sm line-clamp-2">{description}</p>
            
            <div class="flex items-center justify-between mt-4">
                {#if vendorLogo}
                    <div class="flex items-center gap-2">
                        <img src={vendorLogo} alt={vendor} class="h-6 w-6 rounded" />
                        <span class="text-xs text-slate-500">{vendor}</span>
                    </div>
                {:else}
                    <span class="text-xs text-slate-500">{vendor}</span>
                {/if}
                <div class="text-sm text-blue-400 font-medium flex items-center">
                    <span>View details</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1 transform transition-transform duration-300 group-hover:translate-x-2" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </div>
            </div>
        </div>
    </div>
</div>
