<script lang="ts">
    export let onSearch: (query: string) => void = () => {};
    let searchQuery = "";

    function handleSearch() {
        onSearch(searchQuery);
    }

    function handleKeyPress(event: KeyboardEvent) {
        if (event.key === 'Enter') {
            handleSearch();
        }
    }
</script>

<div class="w-full max-w-4xl mx-auto mb-8">
    <div class="relative">
        <div class="absolute inset-y-0 left-0 flex items-center pl-4 pointer-events-none">
            <svg class="w-5 h-5 text-lime-400 drop-shadow-[0_0_4px_rgba(190,242,100,0.8)]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
        </div>
        <input
            type="text"
            bind:value={searchQuery}
            on:keypress={handleKeyPress}
            placeholder="Search MCP servers..."
            class="w-full pl-12 pr-4 py-4 bg-slate-800/60 backdrop-blur-sm border border-cyan-500/50 shadow-lg shadow-cyan-500/20 rounded-xl text-lime-300 placeholder-pink-400 focus:outline-none focus:ring-2 focus:ring-fuchsia-500 focus:border-fuchsia-500 transition-all duration-300"
        />
    </div>
</div>
