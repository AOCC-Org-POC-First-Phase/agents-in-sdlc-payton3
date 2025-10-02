<script lang="ts">
    export let title: string;
    export let description: string;
    export let type: string; // "Local" or "Remote"
    export let vendor: string;
    export let vendorLogo: string = "";
</script>

<div class="group block bg-slate-800/60 backdrop-blur-sm rounded-xl overflow-hidden shadow-lg shadow-cyan-500/20 border border-cyan-500/50 hover:border-fuchsia-500 hover:shadow-fuchsia-500/40 hover:shadow-2xl transition-all duration-300 hover:translate-y-[-4px]">
    <div class="p-6 relative">
        <div class="absolute inset-0 bg-gradient-to-r from-cyan-500/20 to-fuchsia-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        <div class="relative z-10">
            <div class="flex gap-2 mb-3">
                <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-gradient-to-r from-cyan-500 to-lime-400 text-slate-900 shadow-lg shadow-cyan-500/50">
                    MCP
                </span>
                <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-gradient-to-r from-fuchsia-500 to-pink-400 text-white shadow-lg shadow-fuchsia-500/50">
                    {type}
                </span>
            </div>
            
            <h3 class="text-xl font-semibold text-lime-300 mb-2 group-hover:text-cyan-300 transition-colors drop-shadow-[0_0_8px_rgba(190,242,100,0.5)]">
                {title}
            </h3>
            
            <p class="text-slate-300 mb-4 text-sm line-clamp-2">{description}</p>
            
            <div class="flex items-center justify-between mt-4">
                {#if vendorLogo}
                    <div class="flex items-center gap-2">
                        <img src={vendorLogo} alt={vendor} class="h-6 w-6 rounded" />
                        <span class="text-xs text-yellow-300">{vendor}</span>
                    </div>
                {:else}
                    <span class="text-xs text-yellow-300">{vendor}</span>
                {/if}
                <div class="text-sm text-pink-400 font-medium flex items-center drop-shadow-[0_0_4px_rgba(244,114,182,0.5)]">
                    <span>View details</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1 transform transition-transform duration-300 group-hover:translate-x-2" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </div>
            </div>
        </div>
    </div>
</div>
