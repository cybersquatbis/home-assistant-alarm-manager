import './alarme-manager.js';

const COMMUNITY_VERSION='0.5.0-beta.1';
customElements.whenDefined('alarme-manager-panel').then(()=>{
  const Panel=customElements.get('alarme-manager-panel');
  if(!Panel||Panel.prototype.__am050patched)return;
  Panel.prototype.__am050patched=true;
  const originalRender=Panel.prototype.render;
  Panel.prototype.render=function(...args){
    const result=originalRender.apply(this,args);
    queueMicrotask(()=>{
      const root=this.shadowRoot;
      if(!root)return;
      const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
      let node;
      while((node=walker.nextNode())){
        if(node.nodeValue&&node.nodeValue.includes('0.4.0-beta.1'))node.nodeValue=node.nodeValue.replaceAll('0.4.0-beta.1',COMMUNITY_VERSION);
      }
      const chips=root.querySelector('.chips');
      if(chips&&!chips.querySelector('[data-community-antipet]')){
        const c=this.s?.intrusion_confirmation||{};
        const required=c.required!==false;
        const span=document.createElement('span');
        span.className='chip '+(required?'green':'amber');
        span.dataset.communityAntipet='1';
        span.title=required?'Les réactions Alarme Manager exigent une ouverture protégée récente. Les PIR seuls restent utilisables pour la trajectoire.':'Confirmation par ouvrant désactivée.';
        span.textContent=required?`ANTI-ANIMAL ${Number(c.window_seconds||120)} s`:'ANTI-ANIMAL OFF';
        chips.appendChild(span);
      }
    });
    return result;
  };
});
