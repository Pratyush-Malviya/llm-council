import asyncio
import sys
from backend.council import run_full_council

async def main():
    if len(sys.argv) < 2:
        print('Usage: python cli.py "Your question or architecture problem here"')
        sys.exit(1)
        
    query = ' '.join(sys.argv[1:])
    print('\n--- Querying LLM Council ---')
    print(f'Query: {query}\n')
    
    print('[Stage 1] Collecting independent opinions from council models...')
    stage1, stage2, stage3, meta = await run_full_council(query)
    
    print(f'\nCollected {len(stage1)} responses:')
    for item in stage1:
        print(f"  - {item['model']}")
        
    print('\n[Stage 2] Anonymized Peer Rankings:')
    rankings = meta.get('aggregate_rankings', [])
    for idx, r in enumerate(rankings, 1):
        print(f"  {idx}. {r['model']} (Average Rank: {r['average_rank']})")
        
    print(f"\n[Stage 3] Chairman Synthesis ({stage3.get('model')}):")
    print('------------------------------------------------------------')
    print(stage3.get('response', 'No response'))
    print('------------------------------------------------------------\n')

if __name__ == '__main__':
    asyncio.run(main())
