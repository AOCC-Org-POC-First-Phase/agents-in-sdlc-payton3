<script lang="ts">
    import { onMount } from "svelte";

    interface Game {
        id: number;
        title: string;
        description: string;
        publisher_name?: string;
        category_name?: string;
    }

    export let games: Game[] = [];
    let loading = true;
    let error: string | null = null;

    const fetchGames = async () => {
        loading = true;
        try {
            const response = await fetch('/api/games');
            if(response.ok) {
                games = await response.json();
            } else {
                error = `Failed to fetch data: ${response.status} ${response.statusText}`;
            }
        } catch (err) {
            error = `Error: ${err instanceof Error ? err.message : String(err)}`;
        } finally {
            loading = false;
        }
    };

    onMount(() => {
        fetchGames();
    });
</script>

<div>
    <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400 mb-4">Featured Games</h2>
        <div class="h-0.5 w-16 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full mx-auto mb-4"></div>
        <p class="text-slate-400 text-lg max-w-2xl mx-auto">Discover innovative board games that bring the excitement of software development to your table</p>
    </div>
    
    {#if loading}
        <!-- Enhanced loading animation -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {#each Array(6) as _, i}
                <div class="bg-gradient-to-br from-slate-800/80 to-slate-900/60 backdrop-blur-md rounded-2xl overflow-hidden shadow-xl border border-slate-700/50">
                    <div class="p-8">
                        <div class="animate-pulse">
                            <!-- Icon placeholder -->
                            <div class="float-right w-12 h-12 bg-slate-700/50 rounded-xl mb-4"></div>
                            <!-- Title -->
                            <div class="h-6 bg-slate-700/50 rounded-lg w-3/4 mb-4 clear-right"></div>
                            <!-- Tags -->
                            <div class="flex gap-2 mb-4">
                                <div class="h-6 bg-slate-700/50 rounded-full w-16"></div>
                                <div class="h-6 bg-slate-700/50 rounded-full w-20"></div>
                            </div>
                            <!-- Description lines -->
                            <div class="h-3 bg-slate-700/50 rounded w-full mb-2"></div>
                            <div class="h-3 bg-slate-700/50 rounded w-5/6 mb-4"></div>
                            <div class="h-3 bg-slate-700/50 rounded w-4/6 mb-6"></div>
                            <!-- Progress bar -->
                            <div class="mb-6">
                                <div class="flex justify-between mb-2">
                                    <div class="h-3 bg-slate-700/50 rounded w-20"></div>
                                    <div class="h-3 bg-slate-700/50 rounded w-10"></div>
                                </div>
                                <div class="h-2 bg-slate-700/50 rounded-full w-full"></div>
                            </div>
                            <!-- Bottom section -->
                            <div class="flex justify-between">
                                <div class="h-4 bg-slate-700/50 rounded w-16"></div>
                                <div class="h-4 bg-slate-700/50 rounded w-24"></div>
                            </div>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    {:else if error}
        <!-- Enhanced error display -->
        <div class="text-center py-16 bg-gradient-to-br from-slate-800/50 to-slate-900/30 backdrop-blur-sm rounded-2xl border border-slate-700/50">
            <div class="text-6xl mb-4">⚠️</div>
            <h3 class="text-xl font-semibold text-slate-200 mb-2">Oops! Something went wrong</h3>
            <p class="text-red-400 mb-6">{error}</p>
            <button class="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-medium rounded-xl transition-all duration-300 hover:scale-105">
                Try Again
            </button>
        </div>
    {:else if games.length === 0}
        <!-- Enhanced no games display -->
        <div class="text-center py-16 bg-gradient-to-br from-slate-800/50 to-slate-900/30 backdrop-blur-sm rounded-2xl border border-slate-700/50">
            <div class="text-6xl mb-4">🎮</div>
            <h3 class="text-xl font-semibold text-slate-200 mb-2">No Games Available</h3>
            <p class="text-slate-400 mb-6">Check back soon for exciting new gaming projects!</p>
            <button class="px-6 py-3 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 text-white font-medium rounded-xl transition-all duration-300 hover:scale-105">
                Refresh
            </button>
        </div>
    {:else}
        <!-- game list -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8" data-testid="games-grid">
            {#each games as game (game.id)}
                <a 
                    href={`/game/${game.id}`} 
                    class="group block relative bg-gradient-to-br from-slate-800/80 to-slate-900/60 backdrop-blur-md rounded-2xl overflow-hidden shadow-xl border border-slate-700/50 hover:border-blue-500/50 hover:shadow-2xl hover:shadow-blue-500/20 transition-all duration-500 hover:translate-y-[-8px] hover:scale-[1.02]"
                    data-testid="game-card"
                    data-game-id={game.id}
                    data-game-title={game.title}
                >
                    <!-- Card glow effect -->
                    <div class="absolute inset-0 bg-gradient-to-r from-blue-600/0 via-purple-600/5 to-cyan-600/0 opacity-0 group-hover:opacity-100 transition-all duration-500 rounded-2xl"></div>
                    
                    <!-- Card border glow -->
                    <div class="absolute inset-0 rounded-2xl bg-gradient-to-r from-blue-500/20 to-purple-500/20 opacity-0 group-hover:opacity-100 transition-all duration-500 blur-sm"></div>
                    
                    <div class="relative p-8">
                        <!-- Icon placeholder -->
                        <div class="absolute top-6 right-6 w-12 h-12 bg-gradient-to-br from-blue-500/20 to-purple-500/20 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300">
                            <div class="text-2xl">🎮</div>
                        </div>
                        
                        <div class="relative z-10">
                            <h3 class="text-xl font-bold text-slate-100 mb-4 group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-blue-400 group-hover:to-purple-400 transition-all duration-300 line-clamp-2 pr-16" data-testid="game-title">
                                {game.title}
                            </h3>
                            
                            {#if game.category_name || game.publisher_name}
                                <div class="flex flex-wrap gap-2 mb-4">
                                    {#if game.category_name}
                                        <span class="text-xs font-semibold px-3 py-1.5 rounded-full bg-gradient-to-r from-blue-900/40 to-blue-800/40 border border-blue-700/30 text-blue-300 backdrop-blur-sm" data-testid="game-category">
                                            {game.category_name}
                                        </span>
                                    {/if}
                                    {#if game.publisher_name}
                                        <span class="text-xs font-semibold px-3 py-1.5 rounded-full bg-gradient-to-r from-purple-900/40 to-purple-800/40 border border-purple-700/30 text-purple-300 backdrop-blur-sm" data-testid="game-publisher">
                                            {game.publisher_name}
                                        </span>
                                    {/if}
                                </div>
                            {/if}
                            
                            <p class="text-slate-400 mb-6 text-sm leading-relaxed line-clamp-3" data-testid="game-description">
                                {game.description}
                            </p>
                            
                            <!-- Progress bar mockup -->
                            <div class="mb-6">
                                <div class="flex justify-between items-center mb-2">
                                    <span class="text-xs font-medium text-slate-400">Funding Progress</span>
                                    <span class="text-xs font-bold text-green-400">{Math.floor(Math.random() * 40 + 60)}%</span>
                                </div>
                                <div class="w-full bg-slate-700/50 rounded-full h-2 backdrop-blur-sm">
                                    <div class="bg-gradient-to-r from-green-500 to-emerald-400 h-2 rounded-full transition-all duration-1000 group-hover:shadow-lg group-hover:shadow-green-500/30" 
                                         style="width: {Math.floor(Math.random() * 40 + 60)}%"></div>
                                </div>
                            </div>
                            
                            <div class="flex justify-between items-center">
                                <div class="text-sm">
                                    <div class="font-bold text-green-400">${Math.floor(Math.random() * 50 + 25)}k</div>
                                    <div class="text-slate-500 text-xs">raised</div>
                                </div>
                                <div class="text-sm text-blue-400 font-medium flex items-center group-hover:text-blue-300 transition-colors">
                                    <span>View details</span>
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-2 transform transition-transform duration-300 group-hover:translate-x-2" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                    </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                </a>
            {/each}
        </div>
    {/if}
</div>